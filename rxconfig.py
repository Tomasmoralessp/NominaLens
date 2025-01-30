import reflex as rx

class AppConfig(rx.Config):
    pass

config = AppConfig(
    app_name="NominaLens",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
    tailwind={  # Habilita Tailwind
        "theme": {
            "extend": {
                "colors": {
                    "deepblack": "#000000",
                    "charcoal": "#0a0a0a",
                    "gunmetal": "#1a1a1a",
                    "silver": "#c0c0c0",
                    "highlight": "#3498db",
                }
            }
        }
    }
)
