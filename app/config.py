from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "EduGenie"
    environment: str = "development"

    host: str = "127.0.0.1"
    port: int = 8000

    # Gemini
    gemini_api_key: str | None = None
    gemini_model: str = "gemini-3.8-flash"

    # Optional local explanation model
    local_explanation_model: str = "MBZUAI/LaMini-Flan-T5-783M"
    use_local_explanation_model: bool = False

    # Application limits
    max_input_chars: int = 20000

    # CORS
    cors_origins: str = (
        "http://127.0.0.1:8000,"
        "http://localhost:8000"
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @property
    def cors_origin_list(self) -> list[str]:
        return [
            origin.strip()
            for origin in self.cors_origins.split(",")
            if origin.strip()
        ]


@lru_cache
def get_settings() -> Settings:
    return Settings()