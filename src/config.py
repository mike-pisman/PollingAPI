from pydantic import BaseSettings, EmailStr, Field
from functools import lru_cache
from setuptools_scm import get_version


VERSION = get_version(root='..', relative_to=__file__)


class Settings(BaseSettings):  # type: ignore
    app_name: str = Field(default="University Polling API",
                          title="App Name", description="The name of the API.")
    app_version: str = Field(default=VERSION, title="App Version", description="The version of the API.")
    app_description: str = Field(default=("An Open Source API for creating surveys and polls "
                                          "to assist in university research."),
                                 title="App Description", description="A description of the API.")
    admin_email: EmailStr = Field(default=EmailStr("admin@unipoll.cc"),
                                  title="Admin Email", description="The email address of the admin of the API.")
    mongodb_url: str = Field(default="mongodb://localhost:27017",
                             title="MongoDB URL", description="The URL of the MongoDB database.")
    secrete_key: str = Field(default="secret", title="Secrete Key", description="The secrete key of the API.")

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings() -> Settings:
    return Settings()
