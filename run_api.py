"""
Quick start script for running the Quiz API server.

Usage:
    python run_api.py
    
Or with custom settings:
    python run_api.py --host 0.0.0.0 --port 8080
"""

import uvicorn
import argparse


def main():
    parser = argparse.ArgumentParser(description="Run the Quiz API server")
    parser.add_argument(
        "--host",
        type=str,
        default="127.0.0.1",
        help="Host to bind (default: 127.0.0.1)"
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="Port to bind (default: 8000)"
    )
    parser.add_argument(
        "--reload",
        action="store_true",
        help="Enable auto-reload on code changes"
    )
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("🚀 Starting Quiz API Server")
    print("=" * 60)
    print(f"📍 Server: http://{args.host}:{args.port}")
    print(f"📚 API Docs: http://{args.host}:{args.port}/docs")
    print(f"📖 ReDoc: http://{args.host}:{args.port}/redoc")
    print("=" * 60)
    print("\n💡 Press CTRL+C to stop the server\n")
    
    uvicorn.run(
        "src.api:app",
        host=args.host,
        port=args.port,
        reload=args.reload
    )


if __name__ == "__main__":
    main()