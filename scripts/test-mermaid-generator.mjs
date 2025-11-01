#!/usr/bin/env node
// Simple test for generate-mermaid.mjs
// Run with: node scripts/test-mermaid-generator.mjs

import { promises as fs } from "fs";
import path from "path";
import { fileURLToPath } from "url";
import { spawn } from "child_process";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const root = path.dirname(__dirname);

console.log("Testing Mermaid generator...\n");

// Test 1: Script executes successfully
console.log("Test 1: Running generator...");
const child = spawn("node", [path.join(__dirname, "generate-mermaid.mjs")], {
  cwd: root,
  stdio: "inherit"
});

child.on("close", async (code) => {
  if (code !== 0) {
    console.error(`✗ Generator failed with code ${code}`);
    process.exit(1);
  }
  console.log("✓ Generator executed successfully\n");

  // Test 2: All expected files exist
  console.log("Test 2: Checking output files...");
  const expectedFiles = [
    "mermaid/flowchart.mmd",
    "mermaid/er.mmd",
    "mermaid/architecture.mmd",
    "mermaid/ci-sequence.mmd",
    "mermaid/bpmnish.mmd"
  ];

  let allExist = true;
  for (const file of expectedFiles) {
    const fullPath = path.join(root, file);
    try {
      await fs.access(fullPath);
      console.log(`  ✓ ${file}`);
    } catch {
      console.error(`  ✗ ${file} not found`);
      allExist = false;
    }
  }

  if (!allExist) {
    console.error("\n✗ Some output files are missing");
    process.exit(1);
  }
  console.log("✓ All output files exist\n");

  // Test 3: Files contain expected content
  console.log("Test 3: Validating content...");
  const validations = [
    { file: "mermaid/flowchart.mmd", pattern: /flowchart TB/ },
    { file: "mermaid/er.mmd", pattern: /erDiagram/ },
    { file: "mermaid/architecture.mmd", pattern: /architecture-beta/ },
    { file: "mermaid/ci-sequence.mmd", pattern: /sequenceDiagram/ },
    { file: "mermaid/bpmnish.mmd", pattern: /flowchart LR/ }
  ];

  let allValid = true;
  for (const { file, pattern } of validations) {
    const fullPath = path.join(root, file);
    const content = await fs.readFile(fullPath, "utf8");
    if (pattern.test(content)) {
      console.log(`  ✓ ${file} has correct diagram type`);
    } else {
      console.error(`  ✗ ${file} missing expected pattern`);
      allValid = false;
    }
  }

  if (!allValid) {
    console.error("\n✗ Content validation failed");
    process.exit(1);
  }
  console.log("✓ All content validations passed\n");

  console.log("✅ All tests passed!");
  process.exit(0);
});
