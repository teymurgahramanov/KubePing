# KubePing 1.2.1

- 📋 **Copy results:** Added a copy-to-clipboard button in the results table header. Copies the table as both rich HTML (for spreadsheets and docs) and plain text.
- 🏷️ **Method and Source:** Renamed the probe form "Module" label to "Method" and the results table "Host" column to "Source" for clarity.
- 🐳 **Multi-architecture images:** Web and exporter container images are now built for both `linux/amd64` and `linux/arm64`.
- 🛠️ **Helm chart fixes:** Image tags now use component-prefixed format (`web-<version>`, `exporter-<version>`) and both images point at the unified `teymurgahramanov/kubeping` repository.

For the complete list of changes, see the [changelog](./CHANGELOG.md).