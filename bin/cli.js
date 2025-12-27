#! /usr/bin/env node

import fs from 'fs-extra';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const projectName = process.argv[2] || 'my-new-project';
const targetPath = path.join(process.cwd(), projectName);
const templatePath = path.join(__dirname, '../instructions'); // Folder containing your template files

async function scaffold() {
  try {
    console.log(`🚀 Creating project in ${targetPath}...`);
    await fs.copy(templatePath, targetPath);
    console.log('✅ Project created successfully!');
  } catch (err) {
    console.error('❌ Error:', err);
  }
}

scaffold();
