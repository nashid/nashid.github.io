#!/bin/bash

# Script to preview Jekyll site locally

echo "🚀 Starting local Jekyll preview..."
echo ""

# Check if bundle is installed
if ! command -v bundle &> /dev/null; then
    echo "❌ Bundler is not installed. Please install it first:"
    echo "   gem install bundler"
    exit 1
fi

# Install dependencies if needed
if [ ! -d "vendor/bundle" ]; then
    echo "📦 Installing dependencies (first time setup)..."
    bundle install --path vendor/bundle
    echo ""
fi

# Start Jekyll server
echo "🌐 Starting Jekyll server..."
echo "   Your site will be available at: http://localhost:4000"
echo "   Press Ctrl+C to stop the server"
echo ""

bundle exec jekyll serve --livereload

# Note: --livereload automatically refreshes browser when you make changes
