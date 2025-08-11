# VB.NET ↔ C# Translator Frontend

This is the frontend for the VB.NET to C# code translator, designed to be deployed on GitHub Pages.

## Local Development

1. Install dependencies:
   ```bash
   npm install
   ```

2. Start the development server:
   ```bash
   npm run dev
   ```

3. Open [http://localhost:3000](http://localhost:3000) in your browser.

## Deployment to GitHub Pages

### Automatic Deployment (Recommended)

The project includes a GitHub Actions workflow that automatically deploys to GitHub Pages when you push to the main branch.

1. Ensure your repository is named `vb-to-csharp-translator` and update the GitHub username in the configuration files
2. Go to your repository settings → Pages
3. Set the source to "GitHub Actions"
4. Add the `NEXT_PUBLIC_API_URL` secret in your repository settings:
   - Go to Settings → Secrets and variables → Actions
   - Add a new secret named `NEXT_PUBLIC_API_URL`
   - Set the value to your Vercel backend URL (e.g., `https://your-backend.vercel.app`)

### Manual Deployment

1. Build the project:
   ```bash
   npm run build
   ```

2. The static files will be generated in the `out/` directory

3. Push the contents of the `out/` directory to the `gh-pages` branch

## Environment Variables

- `NEXT_PUBLIC_API_URL`: The URL of your Vercel backend API (set this in GitHub repository secrets for production)

## Configuration

The Next.js configuration is set up for static export with:
- Base path: `/vb-to-csharp-translator` (for GitHub Pages)
- Static export enabled
- Unoptimized images (required for static export)
