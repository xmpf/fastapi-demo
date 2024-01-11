from fastapi.middleware.cors import CORSMiddleware
from Secweb.ContentSecurityPolicy import ContentSecurityPolicy

def add_cors_middleware(app):
    origins = [
        "http://localhost:8080",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def add_csp_middleware(app):
    app.add_middleware(
        ContentSecurityPolicy,
        Option={
            'default-src': ["'self'"],
            'base-uri': ["'self'"],
            'block-all-mixed-content': []
        },
        script_nonce=False,
        style_nonce=False
    )
