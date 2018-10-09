# How to make a GPG-signing commit?

## 1. Install GnuPG, generate the key with command
`gpg --gen-key`

A GPG key generally contains following infomations (something not related with the commit signing process is obmited, such as comments):

1). **Name**;

2). **Email**;

3). **Passphrase** -- !! KEEP IT SECRET !! , Passphrase is used for verifing your identity along with your private key, like a master-password of a database;

4). **Public-key series**, which includes:
- **Cipher text block** -- a plain text block, saves in a file with *.ASC extension, includes the most unabridged, complete information of the public key
- **Fingerprint** -- a string, "short version" of the cipher text block
- **Key ID** -- a string, even "shorter version" of the fingerprint, mostly is the last 16bit/8bit of the fingerprint, for convenience, used in verification

5). **Private-key series**, !! KEEP IT SECRET !!, similar with Public-key series:
- **Cipher text block** !! KEEP IT SECRET !!
- **Fingerprint** !! KEEP IT SECRET !!
- **Key ID** !! KEEP IT SECRET !!

#### Note:
It is possible to 'recover' a Fingerprint and Key ID 'from' Cipher text block, for both Public-key series and Private-key series, as the Cipher text block contains the complete infomation of the two keys. **AS LONG AS** you remember the passphrase (master-password).

## 2. Get your Public-key Cipher text block
Use command `gpg --list-keys` in terminal to take a snapshot of your public key infomation.

The output should contains a tab named 'pub' with a long CAPPED string, that is your **Public-key fingerprint**.

Then `gpg --armor --export [Public-key fingerprint]` should get you the **Public-key Cipher text block** for next step.

## 3. Github Website setup
Go to https://github.com/settings/gpg/new, put your **Public-key Cipher text block** in and confirm.

## 4. git setup in terminal
``` sh
# Incase your GnuPG is not installed in a default folder, to makesure git can found the gpg executive, you need to set before use:
git config --global gpg.program [some_folder\GnuPG\bin\gpg.exe]
# Then set the following:
git config --global user.name=[Name]
git config --global user.email=[Email]
git config --global user.signingkey=[Private-key ID]
git config --global commit.gpgsign-true
# (Optional): list all git configurations:
git config -l
```
## 5. Try commit and it should work
