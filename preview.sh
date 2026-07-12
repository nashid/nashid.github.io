#!/bin/bash

# Script to preview the Jekyll site locally.
#
# `jekyll serve --livereload` opens two ports: the site on 4000 and a separate
# LiveReload server on 35729. If a previous run did not shut the LiveReload
# thread down cleanly, that port stays busy and the next start fails with
# "no acceptor (port is in use or requires root privileges)".
#
# This script frees both ports before starting, and tears Jekyll (plus its
# LiveReload thread) down cleanly whenever the script exits: Ctrl+C, a closed
# terminal, or a normal end.

PORT=4000
LIVERELOAD_PORT=35729

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

# Kill whatever is holding a TCP port (e.g. an orphaned Jekyll from a prior run).
free_port() {
    local port="$1"
    local pids
    pids=$(lsof -ti "tcp:${port}" 2>/dev/null)
    if [ -n "${pids}" ]; then
        echo "🧹 Port ${port} is still in use by a previous run; stopping it..."
        kill ${pids} 2>/dev/null
        sleep 1
        pids=$(lsof -ti "tcp:${port}" 2>/dev/null)
        [ -n "${pids}" ] && kill -9 ${pids} 2>/dev/null
    fi
}

# Clear anything left over from a previous preview before we start.
free_port "${PORT}"
free_port "${LIVERELOAD_PORT}"

# Ensure Jekyll and its LiveReload thread stop when this script exits, however
# it exits. The `cleaned` guard keeps the message from printing twice (the INT
# trap and the EXIT trap both fire on Ctrl+C).
JEKYLL_PID=""
cleaned=0
cleanup() {
    [ "${cleaned}" = "1" ] && return
    cleaned=1
    echo ""
    echo "🛑 Stopping Jekyll preview..."
    [ -n "${JEKYLL_PID}" ] && kill "${JEKYLL_PID}" 2>/dev/null
    free_port "${PORT}"
    free_port "${LIVERELOAD_PORT}"
}
trap cleanup INT TERM HUP EXIT

# Start Jekyll server
echo "🌐 Starting Jekyll server..."
echo "   Your site will be available at: http://localhost:${PORT}"
echo "   Press Ctrl+C to stop the server"
echo ""

# Run in the background so the trap can catch Ctrl+C and tear everything down,
# then wait on it so the script stays in the foreground like before.
# --livereload automatically refreshes the browser when you make changes.
bundle exec jekyll serve --livereload --port "${PORT}" &
JEKYLL_PID=$!
wait "${JEKYLL_PID}"
