# Build Tailwind CSS (static)
1. Install NodeJS (>=18). Then in this folder:
   ```bash
   npm install -D tailwindcss
   npx tailwindcss -c tailwind.config.js -i ./tailwind.input.css -o ./tailwind.css --minify
   ```
2. **Swap in HTML**: Open `index.html` and replace the Tailwind CDN script with:
   ```html
   <link rel="stylesheet" href="tailwind.css">
   ```
   Do the same for `yian_core.html` if it uses Tailwind.
3. Commit both the HTML changes and the generated `tailwind.css`.

# Convert images to WebP
Place your original images in a local folder (e.g., `assets_raw/`) then run:
```bash
python tools/convert_images.py assets_raw/ assets_webp/ 82
```
Then update `<img>` to point to `.webp` files, and consider adding `srcset`/`sizes` for responsive variants.

# Notes
- CDN fallback for Tailwind remains in the HTML with a comment block starting `SWAP_TAILWIND_STATIC` to guide the swap.
- We already added `loading="lazy"`, `decoding="async"`, `fetchpriority="low"` to `<img>` and `defer` to heavy scripts.
- For even smoother 60fps: dynamically import heavy libs only on interaction (hover/click) using `import()`.