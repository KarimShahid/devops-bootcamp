#!/bin/bash

set -e  # exit if any command fails

APP_DIR="myapp"
PKG_NAME="myapp_$(date +%Y%m%d%H%M%S).tar.gz"   # versioned tarball
CHECKSUM_FILE="checksum.txt"

# List of required files
REQUIRED_FILES=(
    "$APP_DIR/package.json"
    "$APP_DIR/package-lock.json"
    "$APP_DIR/tsconfig.json"
)

# List of required directories
REQUIRED_DIRS=(
    "$APP_DIR/src"
)

echo "=== Validating required files ==="

# Check required files
for file in "${REQUIRED_FILES[@]}"; do
    if [ ! -f "$file" ]; then
        echo "❌ ERROR: Required file missing: $file"
        exit 1
    fi
done

# Check required directories
for dir in "${REQUIRED_DIRS[@]}"; do
    if [ ! -d "$dir" ]; then
        echo "❌ ERROR: Required directory missing: $dir"
        exit 1
    fi
done

echo "✅ All required files and directories are present."

echo "=== Creating tarball ==="

tar -czvf "$PKG_NAME" --exclude="$APP_DIR/node_modules" "$APP_DIR"

echo "Package created: $PKG_NAME"

echo "=== Generating checksum ==="

sha256sum "$PKG_NAME" > "$CHECKSUM_FILE"

echo "=== Verifying checksum ==="

sha256sum --check "$CHECKSUM_FILE"

echo "🎉 SUCCESS: Package ready at: $(realpath $PKG_NAME)"
