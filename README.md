# Muninn

Automated OSINT analysis engine for pr-cybr's rav3n-n3t framework — synthesizes collected intelligence into actionable reports prepared for publication by rav3n-net.

## Overview

Muninn (named after Odin's raven of memory) processes OSINT data collected by Huginn and transforms it into actionable intelligence reports. It analyzes the raw data, identifies key findings, and generates comprehensive markdown reports ready for publication by RavenNet.

## Architecture

The Muninn project follows a phased approach:

- **Phase 1**: Project scaffolding and structure (Current)
- **Phase 2**: Data ingestion from Huginn and AI-powered analysis
- **Phase 3**: Report generation and formatting for RavenNet

### Component Flow

```
Huginn (Data Collection) → Muninn (Analysis) → RavenNet (Publishing)
```

## Project Structure

```
muninn/
├── src/
│   └── muninn/
│       ├── __init__.py
│       ├── analyze.py          # Main analysis orchestration
│       ├── data_loader.py      # Load Huginn output data
│       ├── summarizer.py       # AI-powered summarization
│       └── report_generator.py # Markdown report generation
├── data/
│   ├── input/                  # Huginn output data
│   └── output/                 # Generated reports
├── config/
│   └── config.yaml            # Configuration settings
├── tests/
│   └── test_analyze.py
├── requirements.txt
├── setup.py
└── README.md
```

## Installation

```bash
# Clone the repository
git clone https://github.com/PR-CYBR/muninn.git
cd muninn

# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .
```

## Usage

### Basic Analysis

```bash
# Analyze Huginn data and generate report
python -m muninn.analyze --input data/input/huginn_output.json --output data/output/report.md
```

### Configuration

Edit `config/config.yaml` to customize:
- AI model settings
- Report formatting preferences
- Data source locations
- Analysis parameters

## Input Data Format

Muninn expects Huginn data in JSON format:

```json
{
  "sources": [
    {
      "type": "web",
      "url": "https://example.com",
      "content": "...",
      "timestamp": "2025-10-31T12:00:00Z",
      "metadata": {}
    }
  ]
}
```

## Output Format

Generated reports are in Markdown format with sections:
- Executive Summary
- Key Findings
- Detailed Analysis
- Sources and References
- Recommendations

## Development

### Phase 1 (Current)
- ✅ Project structure scaffolding
- ✅ Placeholder scripts
- ✅ Documentation

### Phase 2 (Planned)
- [ ] Huginn data loader implementation
- [ ] AI model integration (self-hosted/free)
- [ ] Analysis engine
- [ ] Key findings extraction

### Phase 3 (Planned)
- [ ] Report template system
- [ ] Markdown generation
- [ ] RavenNet integration
- [ ] Automated publishing workflow

## Contributing

This project is part of the pr-cybr rav3n-n3t framework. Contributions should align with the overall architecture and security practices.

## License

[To be determined]

## Related Projects

- **Huginn**: OSINT data collection
- **RavenNet**: Intelligence report publishing platform
