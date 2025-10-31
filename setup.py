"""Setup configuration for Muninn OSINT Analysis Engine."""

from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

setup(
    name="muninn",
    version="0.1.0",
    author="PR-CYBR",
    author_email="",
    description="Automated OSINT analysis engine for rav3n-n3t framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PR-CYBR/muninn",
    project_urls={
        "Bug Reports": "https://github.com/PR-CYBR/muninn/issues",
        "Source": "https://github.com/PR-CYBR/muninn",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pyyaml>=6.0.1",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.4.0",
        ],
        "ollama": [
            "ollama-python>=0.1.0",
        ],
        "full": [
            "transformers>=4.30.0",
            "torch>=2.0.0",
            "nltk>=3.8.0",
            "pandas>=2.0.0",
            "numpy>=1.24.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "muninn=muninn.analyze:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
