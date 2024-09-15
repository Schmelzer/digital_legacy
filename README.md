# Digital Legacy Key and Password Generator
This project contains a Python script designed to create or recreate a key and password used to manage a digital legacy. It creates a BIP39 seed phrase (also known as a mnemonic phrase) and derives a master password from it. The script also generates recovery cards that allow you to recover the passphrase by combining at least two cards.

## Features
- Generate a BIP39 seed phrase (mnemonic phrase) with a strength of 256 bits.
- Option to recreate a BIP39 seed phrase by providing an existing word list as a command-line argument.
- Derive a master password from the BIP39 seed in base64
- Create recovery cards that split the mnemonic phrase into parts, with partial words hidden as XXXX.

# Setup
```bash
git clone https://github.com/Schmelzer/digital_legacy
cd digital_legacy

pip install -r requirements.txt
```
# Usage
1. Generating a New Key and Password

	To generate a new BIP39 seed phrase (mnemonic) and derive the master password, simply run the script without any arguments:
	```bash
	python digital_legacy.py
	```

2. Reusing an Existing Seed Phrase

	If you already have a BIP39 seed phrase, pass it as command-line arguments. For example:
	```bash
	python digital_legacy.py panic afraid alarm noodle correct proof skate duty during banner chuckle answer push firm remind march phone snake lawsuit increase hello place know ensure
	```
	The script will then regenerate the BIP39 seed and master password based on the provided words.

3. Output

	The script will print:

	* The **BIP39 seed phrase** (either generated or provided).
	* The **BIP39 seed** in both **hex** and **base64** formats.
	* The **Master password** (a 12-character password derived from the BIP39 seed).
	* **Three recovery cards** that can be used to recover the seed phrase by combining any two cards.

	Example output:
	```
	Word list: organ catalog scale window million clap column popular size pigeon wash option margin chaos office before volcano hard seek spawn local shrimp drive behind
	BIP39 seed (hex): 112fbd6f02301728a2382bed15dd9d8a7c84961821b49932ad5f13a238b9e6476ad67697e4ad056b4fb32998c9179321af0fbe9fdee88b1f6f29fbed79fd6f9c
	BIP39 seed (base64): ES+9bwIwFyiiOCvtFd2dinyElhghtJkyrV8Toji55kdq1naX5K0Fa0+zKZjJF5Mhrw++n97oix9vKfvtef1vnA==
	Password vx3xRJubKtET
	Card 1: organ XXXX scale XXXX XXXX clap XXXX popular size XXXX wash option margin chaos XXXX before volcano XXXX seek spawn local XXXX drive behind
	Card 2: organ catalog XXXX window million XXXX column popular XXXX pigeon wash XXXX margin XXXX office XXXX volcano hard seek XXXX local shrimp XXXX behind
	Card 3: XXXX catalog scale window million clap column XXXX size pigeon XXXX option XXXX chaos office before XXXX hard XXXX spawn XXXX shrimp drive XXXX
	```

# License
This project is licensed under the MIT License.
