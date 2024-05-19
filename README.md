
# Utility Python Scripts

Welcome to the Utility Python Scripts repository! This repository contains various utility scripts that can help you with different tasks such as copying files, setting up hydration reminders, generating passwords, managing task reminders, analyzing websites, and counting words in text files.

## Directory Structure

```
.
├── copy-file
│   └── app.py
|   └── demo.txt
│   └── copied.py
├── hydration-reminder
│   └── app.py
│   └── notification_sound.mp3
├── password-generator
│   └── app.py
├── task-reminder-system
│   └── app.py
│   └── reminder_sound.mp3
│   └── reminder_finish_task.mp3
├── web-sleuth
│   └── app.py
│   └── .env
├── word-count
│   └── app.py
│   └── demo.txt
├── .gitignore
├── requirements.txt
└── README.md

```

## Getting Started

### Prerequisites

Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

### Installation

1. Clone the repository:

```sh
git clone https://github.com/yourusername/Utility-Python-Scripts.git
cd Utility-Python-Scripts
```

2. Install the required Python packages:

```sh
pip install -r requirements.txt
```

## Scripts Overview

### 1. Copy File

This script copies a file from one location to another.

**Running the script:**

```sh
cd copy-file
python app.py
```

### 2. Hydration Reminder

This script reminds you to stay hydrated at regular intervals.

**Running the script:**

```sh
cd hydration-reminder
python app.py
```

### 3. Password Generator

This script generates a random, secure password.

**Running the script:**

```sh
cd password-generator
python app.py
```

### 4. Task Reminder System

This script sets up reminders for your tasks at specified times.

**Running the script:**

```sh
cd task-reminder-system
python app.py
```

### 5. Web Sleuth

This script analyzes a given website and provides basic information, technology stack, WHOIS information, IP address, and geolocation details.

**Running the script:**

1. Create a `.env` file in the `web-sleuth` directory with the following content:
   
```
API_KEY=your_ipinfo_api_key
```

2. Run the script:

```sh
cd web-sleuth
python app.py
```

### 6. Word Count

This script counts the number of words in a given text file.

**Running the script:**

```sh
cd word-count
python app.py
```

## Contributing

Feel free to submit pull requests to contribute to the project. For major changes, please open an issue first to discuss what you would like to change.
