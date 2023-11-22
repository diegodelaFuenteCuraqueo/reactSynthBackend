# ReactSynth Backend

A Flask application that serves as an API to manage synth presets for the [ReactSynth](https://github.com/diegodelaFuenteCuraqueo/reactsynth) project.

## Table of Contents

- [Introduction](#introduction)
- [Setup](#setup)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This is a Flask application that serves as an API to manage synth presets. It provides endpoints to perform CRUD operations on synth presets stored in a MySQL database.

Each preset is a JSON object with the following structure:

```json
{
  "name": "Preset 1",
  "modulation_index": 1.5,
  "harmonicity": 2.0,
  "low_key": 20,
  "number_of_keys": 88
}
```

### Prerequisites

- Python 3.x
- MySQL
