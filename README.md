# KamiIntel Agent

A sophisticated AI-powered knowledge assistant focused on energy solutions and course generation.

## 🌟 Features

- **Interactive Chat Interface**: Ask questions and receive AI-generated responses based on your knowledge base
- **Document Training**: Upload and train the system on PDF, DOCX, TXT, Excel, and PowerPoint files
- **Multi-language Support**: Generate content in English, Kiswahili, French, German, and Amharic
- **Course Generation**: Create comprehensive training course outlines with learning objectives, activities, and assessments
- **Report Generation**: Generate professional reports with structured sections
- **PowerPoint Creation**: Automatically create slide decks with customizable themes
- **Data Analysis**: Upload and analyze CSV files with automatic summary generation

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- OpenAI API key

### Installation

1. Clone this repository or download the ZIP file
2. Navigate to the project directory
3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

1. Set up your OpenAI API key:
   - Create a `.env` file in the project root directory
   - Add your API key: `OPENAI_API_KEY=your-api-key-here`
   - Or set it as an environment variable: `set OPENAI_API_KEY=your-api-key-here` (Windows)

### Running the Application

Run the application using the start script:

```bash
start_kamiintel.bat
```

Or directly with Python:

```bash
python app.py
```

The application will start on <http://127.0.0.1:8002> by default.

## 📚 Usage Guide

### Chat Interface

![Chat Interface](https://i.imgur.com/example-chat.png) <!-- Add a real screenshot here -->

- Type your question in the chat box and select your preferred language
- Use special commands like "Write a report about..." or "Generate PowerPoint slides about..." for specialized outputs
- Click "Explain Like I'm 5" for simplified explanations
- Export responses to Word documents with a single click

### Training the System

1. Navigate to the "Upload & Train" section
2. Upload your documents (PDF, DOCX, TXT, Excel, PowerPoint)
3. Click "Train from File" to process individual files or "Train All Uploaded Files" for batch processing

### Course Generation

1. Go to "Generate Course Outline"
2. Enter your course topic
3. Optionally select a category
4. The system will create a comprehensive course outline with:
   - TXT version
   - DOCX document
   - PowerPoint presentation

### Slide Generation

1. Navigate to "Generate Slides"
2. Enter your presentation topic
3. Customize theme colors and other settings
4. Add optional chart data or images
5. Download the generated PowerPoint file

## 📋 File Organization

- `/chat_data/`: Stores all user data and generated content
  - `/generated_courses/`: Course outlines in multiple formats
  - `/generated_reports/`: Reports, CSVs, and presentations
  - `/uploads/`: User-uploaded training documents
  - `/vector_store/`: Vector embeddings of trained documents
  - `/prompts/`: Stored user prompts
  - `/responses/`: Stored AI responses
  - `/logs/`: Application logs for troubleshooting
  - `/raw_data/`: Temporary storage for uploaded data
- `/templates/`: HTML templates for the web interface
- `/agent_utils/`: Utility functions for memory management and vector storage
- `/static/`: Static assets for the web interface

## 🔧 Troubleshooting

- **File Upload Issues**: Ensure files are under 10MB and in supported formats
- **Generation Errors**: Check the application logs in chat_data/logs
- **No Relevant Answers**: Try uploading more relevant training documents
- **OpenAI API Issues**: Verify your API key is correctly set and has sufficient quota

## 🔒 Security Features

- MIME type validation for uploads
- File size restrictions (10MB maximum)
- Path traversal prevention
- Sanitized filenames
- Binary file handling protection

## 🖥️ Technical Details

- Built with Flask web framework
- Uses LangChain for vector search and document processing
- Powered by OpenAI GPT models
- Document embeddings stored using FAISS vector database

## 📝 License

MIT License

Copyright (c) 2025 KamiIntel

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

## 📬 Contact

For technical support or inquiries, please contact:

- Email: <support@kamiintel.com>
- Website: <https://kamiintel.com>
- GitHub: <https://github.com/kamiintel>

<!-- Replace the above with your actual contact information -->