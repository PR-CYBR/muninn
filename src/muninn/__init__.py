"""
Muninn - Automated OSINT Analysis Engine

This package processes OSINT data collected by Huginn and transforms it into
actionable intelligence reports for publication by RavenNet.
"""

__version__ = "0.1.0"
__author__ = "PR-CYBR"

from .analyze import analyze_data
from .data_loader import load_huginn_data
from .summarizer import summarize_findings
from .report_generator import generate_report

__all__ = [
    "analyze_data",
    "load_huginn_data",
    "summarize_findings",
    "generate_report",
]
