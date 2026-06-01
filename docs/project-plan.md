# Project Plan

## Project idea
Build a program that accepts an amino acid sequence, predicts a possible ligand-binding pocket, and estimates how binding at that pocket may affect ammonium ion transport.

## Version 1 objective
Create a simple prototype that:
- accepts a protein sequence input,
- checks whether the sequence may belong to an ammonium transporter-related protein,
- predicts or displays a candidate binding pocket,
- gives a basic explanation of how binding could affect ammonium transport.

## Main steps
1. Collect sequence input from the user.
2. Convert sequence into a usable protein structure source or model.
3. Run pocket prediction on the structure.
4. Show the pocket visually.
5. Add a basic transport-effect interpretation.
6. Test with one known ammonium transporter example.

## Initial folders
- `frontend/` for user interface
- `backend/` for prediction logic
- `data/` for sample sequences and structures
- `tests/` for checking results
- `docs/` for planning and notes

## Current status
Version 1 planning stage.
