# SDK Publishing Plan (Registries)

## Targets
- PyPI: `bridgetrace-sdk`
- npm: `@bridgetrace/sdk-js`
- crates.io: `bridgetrace-sdk-rs`

## Python (PyPI)
```bash
cd sdk/python
python -m build
python -m twine upload dist/*
```

## JavaScript (npm)
```bash
cd sdk/js
npm publish --access public
```

## Rust (crates.io)
```bash
cd sdk/rust
cargo publish
```

## Trust Signal
After publication, add registry badges in README with version pins.
