import sys

from app import create_app


def print_banner(app):
    print("=" * 50)
    print(f"🚀 Backend running on http://localhost:{app.config['PORT']} (debug={app.config['DEBUG']})")
    print("=" * 50)
    print("Available Routes:")
    seen = set()
    for rule in sorted(app.url_map.iter_rules(), key=lambda r: (str(r.rule), str(list(r.methods)))):
        if rule.endpoint == "static":
            continue
        methods = ",".join(sorted(m for m in rule.methods if m not in ("HEAD", "OPTIONS")))
        entry = f"  - {methods} {rule.rule}"
        if entry not in seen:
            print(entry)
            seen.add(entry)
    print("=" * 50)


if __name__ == "__main__":
    app = create_app()
    try:
        print_banner(app)
        app.run(debug=app.config["DEBUG"], port=app.config["PORT"], host="0.0.0.0")
    except OSError as exc:
        print("Failed to start server:", exc)
        print("If you see a socket/permission error, pick a different port and set SAFE_COMPLY_PORT or free the port.")
        sys.exit(1)
