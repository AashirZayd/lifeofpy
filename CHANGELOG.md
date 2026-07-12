# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0-alpha] - 2026-07-13

### Added
- **Engine**: Core execution framework decoupled from I/O.
- **Registry Provider**: Pluggable architecture supporting GitHub, Local, and Mirror providers.
- **Manifest Validator**: Strict diagnostic engine enforcing schema and semantic versioning rules.
- **Registry Builder**: Deterministic pipeline (Discover -> Validate -> Resolve -> Sort -> Checksum).
- **Dependency Graph Engine**: Graph-based resolver with DFS cycle detection and framework conflict resolution.
- **Downloader Engine**: Transport-agnostic queue-based downloader with isolated staging and cryptographic verification.
- **Installer Engine**: Transactional orchestration layer featuring atomic commits, rollback recovery, and history state generation.
