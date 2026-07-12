<div align="center">
  <h1>🚀 LifeOfPy</h1>
  <p><b>Beautiful UI Components for Python.</b></p>

  <p>
    <a href="https://github.com/lifeofpy/lifeofpy/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License"></a>
    <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/Python-3.12%2B-blue.svg" alt="Python 3.12+"></a>
    <a href="https://github.com/lifeofpy/lifeofpy/actions"><img src="https://img.shields.io/badge/Build-Passing-brightgreen.svg" alt="Build"></a>
    <a href="https://github.com/lifeofpy/lifeofpy"><img src="https://img.shields.io/badge/Registry-v1.0-orange.svg" alt="Registry v1.0"></a>
    <a href="https://github.com/lifeofpy/lifeofpy"><img src="https://img.shields.io/badge/Engine-v0.1.0-purple.svg" alt="Engine v0.1.0"></a>
    <a href="https://github.com/lifeofpy/lifeofpy/stargazers"><img src="https://img.shields.io/github/stars/lifeofpy/lifeofpy?style=social" alt="Stars"></a>
  </p>
</div>

## 🌟 Why LifeOfPy?

LifeOfPy brings the modern component-driven development experience to the Python ecosystem. Instead of installing bloated UI libraries that are hard to customize, you copy and paste beautiful, accessible components directly into your project via our CLI.

- **Component Registry**: Browse and search a massive collection of curated UI components for frameworks like CustomTkinter, PyQt, and Textual.
- **CLI**: A blazing fast CLI to add, update, and manage your components.
- **Deterministic Installs**: A robust Dependency Graph engine guarantees that components and their dependencies are installed perfectly every time.
- **Checksum Verification**: Every download is cryptographically verified against the registry to ensure your code is secure.
- **Rollback Safety**: If an installation fails mid-way, the Installer seamlessly rolls back to prevent a broken state.
- **Community Driven**: Built entirely open-source, allowing anyone to submit components, frameworks, or registry improvements.

## 🚀 Installation

```bash
pip install lifeofpy-cli
```

## 🛠️ Usage

Initialize LifeOfPy in your Python project:

```bash
lifeofpy init
```

Add a beautiful modern button to your project:

```bash
lifeofpy add button-modern
```

## 🏗️ Architecture

LifeOfPy is built on a decoupled, production-grade engine architecture.

```text
Developer
   ↓
  CLI
   ↓
Installer
   ↓
Dependency Graph
   ↓
Downloader
   ↓
Registry Provider
   ↓
 Registry
```

## 🗺️ Roadmap

- [x] Engine V1
- [x] Registry Architecture
- [ ] CLI V1
- [ ] Initial Reference Components
- [ ] Website & Explorer
- [ ] Public Beta

For a detailed breakdown, see our [ROADMAP.md](ROADMAP.md).

## 🤝 Contributing

We love contributions! Please read our [Contributing Guide](CONTRIBUTING.md) to get started with setting up the project, our coding conventions, and how to submit a pull request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">
  <sub>Built for the Python community ❤️</sub>
</div>
