"""
Report generation module for creating formatted Markdown reports.

This module generates professional intelligence reports in Markdown format
ready for publication by RavenNet.
"""

import logging
from datetime import datetime
from typing import Dict, List, Any, Optional

logger = logging.getLogger(__name__)


class ReportGenerator:
    """
    Generates formatted Markdown intelligence reports.
    
    Phase 1: Basic report structure.
    Phase 3: Will implement full template system and formatting.
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialize the report generator.
        
        Args:
            config: Configuration dictionary with report settings
        """
        self.config = config or {}
        self.template = self.config.get('template', 'default')
        logger.info(f"Initialized report generator with template: {self.template}")
    
    def generate(self, data: Dict[str, Any], analysis: Dict[str, Any]) -> str:
        """
        Generate complete intelligence report.
        
        Args:
            data: Raw data from Huginn
            analysis: Analysis results from summarizer
        
        Returns:
            Formatted Markdown report string
        """
        logger.info("Generating intelligence report")
        
        sections = [
            self._generate_header(data),
            self._generate_executive_summary(analysis),
            self._generate_key_findings(analysis),
            self._generate_detailed_analysis(data, analysis),
            self._generate_sources(data),
            self._generate_recommendations(analysis),
            self._generate_footer()
        ]
        
        return "\n\n".join(sections)
    
    def _generate_header(self, data: Dict[str, Any]) -> str:
        """Generate report header."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
        
        header = f"""# Intelligence Report

**Generated:** {timestamp}  
**Collection ID:** {data.get('collection_id', 'N/A')}  
**Status:** {data.get('metadata', {}).get('status', 'Complete')}

---"""
        
        return header
    
    def _generate_executive_summary(self, analysis: Dict[str, Any]) -> str:
        """Generate executive summary section."""
        summary_text = analysis.get('summary', 'No summary available.')
        
        section = f"""## Executive Summary

{summary_text}"""
        
        return section
    
    def _generate_key_findings(self, analysis: Dict[str, Any]) -> str:
        """Generate key findings section."""
        findings = analysis.get('key_findings', [])
        
        if not findings:
            findings_text = "*No key findings identified.*"
        else:
            findings_text = "\n".join([f"- {finding}" for finding in findings])
        
        section = f"""## Key Findings

{findings_text}"""
        
        return section
    
    def _generate_detailed_analysis(self, data: Dict[str, Any], analysis: Dict[str, Any]) -> str:
        """Generate detailed analysis section."""
        themes = analysis.get('themes', [])
        source_count = len(data.get('sources', []))
        
        themes_text = "\n".join([f"- {theme}" for theme in themes]) if themes else "*No themes identified.*"
        
        section = f"""## Detailed Analysis

### Overview

This analysis is based on {source_count} OSINT sources collected by Huginn.

### Identified Themes

{themes_text}

### Analysis Methodology

*Phase 2 will include detailed methodology description.*"""
        
        return section
    
    def _generate_sources(self, data: Dict[str, Any]) -> str:
        """Generate sources and references section."""
        sources = data.get('sources', [])
        
        if not sources:
            sources_text = "*No sources available.*"
        else:
            sources_list = []
            for idx, source in enumerate(sources, 1):
                source_type = source.get('type', 'unknown')
                url = source.get('url', 'N/A')
                timestamp = source.get('timestamp', 'N/A')
                sources_list.append(f"{idx}. **{source_type.title()}**: {url} (collected: {timestamp})")
            
            sources_text = "\n".join(sources_list)
        
        section = f"""## Sources and References

{sources_text}"""
        
        return section
    
    def _generate_recommendations(self, analysis: Dict[str, Any]) -> str:
        """Generate recommendations section."""
        recommendations = analysis.get('recommendations', [])
        
        if not recommendations:
            rec_text = "*No recommendations available.*"
        else:
            rec_text = "\n".join([f"{idx}. {rec}" for idx, rec in enumerate(recommendations, 1)])
        
        section = f"""## Recommendations

{rec_text}"""
        
        return section
    
    def _generate_footer(self) -> str:
        """Generate report footer."""
        footer = """---

*This report was automatically generated by Muninn, the OSINT analysis engine for PR-CYBR's rav3n-n3t framework.*

**Next Steps:**
- Review findings and recommendations
- Validate sources and analysis
- Publish via RavenNet platform

**For Questions or Feedback:**
- Contact: pr-cybr team
- Framework: rav3n-n3t"""
        
        return footer
    
    def save_to_file(self, report: str, output_path: str) -> None:
        """
        Save report to file.
        
        Args:
            report: Markdown report content
            output_path: Path where report will be saved
        """
        from pathlib import Path
        
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        output_file.write_text(report, encoding='utf-8')
        
        logger.info(f"Report saved to {output_path}")


def generate_report(data: Dict[str, Any], analysis: Dict[str, Any], 
                   output_path: str, config: Optional[Dict[str, Any]] = None) -> str:
    """
    Convenience function to generate and save a report.
    
    Args:
        data: Raw data from Huginn
        analysis: Analysis results from summarizer
        output_path: Path where report will be saved
        config: Optional configuration dictionary
    
    Returns:
        Generated report content
    """
    generator = ReportGenerator(config)
    report = generator.generate(data, analysis)
    generator.save_to_file(report, output_path)
    
    return report
