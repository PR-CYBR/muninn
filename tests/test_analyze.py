"""
Test suite for Muninn analysis module.

Phase 1: Basic smoke tests to verify module structure.
Phase 2: Will add comprehensive tests for analysis functionality.
"""

import pytest
import sys
from pathlib import Path

# Add src to path for imports
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from muninn import __version__
from muninn.analyze import analyze_data
from muninn.data_loader import load_huginn_data, HuginDataLoader
from muninn.summarizer import summarize_findings, IntelligenceSummarizer
from muninn.report_generator import generate_report, ReportGenerator


def test_version():
    """Test that version is defined."""
    assert __version__ == "0.1.0"


def test_imports():
    """Test that all modules can be imported."""
    from muninn import analyze_data, load_huginn_data, summarize_findings, generate_report
    assert callable(analyze_data)
    assert callable(load_huginn_data)
    assert callable(summarize_findings)
    assert callable(generate_report)


def test_data_loader_init():
    """Test HuginDataLoader initialization."""
    loader = HuginDataLoader("test.json")
    assert loader.file_path.name == "test.json"
    assert loader.data is None


def test_summarizer_init():
    """Test IntelligenceSummarizer initialization."""
    summarizer = IntelligenceSummarizer()
    assert summarizer.model_type == "ollama"
    
    config = {"model_type": "gpt4all"}
    summarizer = IntelligenceSummarizer(config)
    assert summarizer.model_type == "gpt4all"


def test_report_generator_init():
    """Test ReportGenerator initialization."""
    generator = ReportGenerator()
    assert generator.template == "default"
    
    config = {"template": "detailed"}
    generator = ReportGenerator(config)
    assert generator.template == "detailed"


def test_analyze_sources():
    """Test basic source analysis."""
    summarizer = IntelligenceSummarizer()
    sources = [
        {"type": "web", "url": "https://example.com", "content": "test"}
    ]
    
    analysis = summarizer.analyze_sources(sources)
    assert "total_sources" in analysis
    assert analysis["total_sources"] == 1
    assert "key_findings" in analysis
    assert "themes" in analysis
    assert "recommendations" in analysis


def test_report_generation():
    """Test basic report generation."""
    generator = ReportGenerator()
    
    data = {
        "collection_id": "test_001",
        "sources": [
            {"type": "web", "url": "https://example.com", "timestamp": "2025-10-31"}
        ],
        "metadata": {"status": "complete"}
    }
    
    analysis = {
        "summary": "Test summary",
        "key_findings": ["Finding 1", "Finding 2"],
        "themes": ["Theme 1"],
        "recommendations": ["Recommendation 1"]
    }
    
    report = generator.generate(data, analysis)
    assert "# Intelligence Report" in report
    assert "## Executive Summary" in report
    assert "## Key Findings" in report
    assert "Test summary" in report


def test_summarize_findings():
    """Test summarize_findings convenience function."""
    sources = [
        {"type": "web", "url": "https://example.com", "content": "test content"}
    ]
    
    result = summarize_findings(sources)
    assert "analysis" in result
    assert "summary" in result
    assert "key_findings" in result
    assert "themes" in result
    assert "recommendations" in result


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
