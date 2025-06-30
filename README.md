# Harmonised-code-
# 📊 HS Code Tree Extractor

This Python project extracts and organizes **Harmonized System (HS) codes** from a government-issued **tariff PDF** into a clean Excel file structured as a **hierarchical tree format**:

- HS-2 → Chapter  
- HS-4 → Heading  
- HS-6 → Subheading  
- HS-8/10 → Optional deeper levels  

The output is designed to match the format of BTKI or WCO-style HS trees.

---

## 🔍 What It Does

✅ Parses a local HS tariff PDF (e.g., from Bea Cukai / Indonesian Customs)  
✅ Skips noise lines at the top (e.g., page headers, titles)  
✅ Detects and structures HS codes by level:  
 • **Chapter** (HS-2)  
 • **Heading** (HS-4)  
 • **Subheading** (HS-6)  
✅ Outputs a clean Excel file with a tree view layout

---

## 📦 Project Structure

