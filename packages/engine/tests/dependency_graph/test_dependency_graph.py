import pytest
from core.logging.logger import DefaultLogger
from engine.dependency_graph.models import DependencyNode
from engine.dependency_graph.service import DependencyGraphService


@pytest.fixture
def logger():
    return DefaultLogger()


@pytest.fixture
def service(logger):
    return DependencyGraphService(logger)


def test_successful_resolution(service):
    available_nodes = {
        "button": DependencyNode(
            id="button", version="1.0.0", frameworks=["customtkinter"], dependencies=["label", "icon"]
        ),
        "label": DependencyNode(id="label", version="1.0.0", frameworks=["customtkinter"], dependencies=[]),
        "icon": DependencyNode(id="icon", version="1.0.0", frameworks=["customtkinter"], dependencies=[]),
    }

    requested = [available_nodes["button"]]

    resolution = service.resolve(requested, available_nodes, target_framework="customtkinter")

    assert not resolution.has_errors
    assert len(resolution.resolved_nodes) == 3

    plan = service.plan(resolution)

    assert plan.total_components == 3
    download_stage = plan.stages[1]
    assert download_stage.components[0] in ["label", "icon"]
    assert download_stage.components[1] in ["label", "icon"]
    assert download_stage.components[2] == "button"


def test_missing_dependency(service):
    available_nodes = {
        "button": DependencyNode(
            id="button", version="1.0.0", frameworks=["customtkinter"], dependencies=["label", "icon"]
        ),
        "icon": DependencyNode(id="icon", version="1.0.0", frameworks=["customtkinter"], dependencies=[]),
    }

    requested = [available_nodes["button"]]
    resolution = service.resolve(requested, available_nodes)

    assert resolution.has_errors
    assert any(d.code == "DEP-RES-001" for d in resolution.diagnostics)


def test_circular_dependency(service):
    available_nodes = {
        "a": DependencyNode(id="a", version="1.0.0", frameworks=["customtkinter"], dependencies=["b"]),
        "b": DependencyNode(id="b", version="1.0.0", frameworks=["customtkinter"], dependencies=["a"]),
    }

    requested = [available_nodes["a"]]
    resolution = service.resolve(requested, available_nodes)

    assert resolution.has_errors
    assert any(d.code == "DEP-CYC-001" for d in resolution.diagnostics)


def test_framework_mismatch(service):
    available_nodes = {"button": DependencyNode(id="button", version="1.0.0", frameworks=["tkinter"], dependencies=[])}

    requested = [available_nodes["button"]]
    resolution = service.resolve(requested, available_nodes, target_framework="customtkinter")

    assert resolution.has_errors
    assert any(d.code == "DEP-CNF-001" for d in resolution.diagnostics)
