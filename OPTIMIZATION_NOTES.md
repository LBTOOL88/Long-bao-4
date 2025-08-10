# Long-bao-4 optimized (UI & features preserved)

- Added `dns-prefetch` + `preconnect` for all external origins to reduce mobile startup latency.
- Replaced `setInterval(drawMatrix, 33)` with a `requestAnimationFrame` loop tuned to ~30fps and paused when tab is hidden (no visual change to the matrix effect, lower jank/battery).
- Set `decoding="async"` on images and `fetchpriority="high"` on the first image (keeps visual identical, improves LCP). Other images default to lazy loading if not already set.
- Kept **all CSS effects** (blur, backdrop-filter, animations) and **kept script order** so behavior and UI remain the same.