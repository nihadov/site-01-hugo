# Dubai Calligrapher Directory

A curated, verified reference directory of UAE-based Arabic calligraphers.

## Project Structure
- `content/calligraphers/`: Individual calligrapher profile pages.
- `data/calligraphers.json`: The source dataset for calligraphers.
- `layouts/`: Custom Hugo templates for the directory.
- `static/img/`: Placeholder images for portraits and artwork.

## How to Manage Content

### Adding a New Calligrapher
1. Add the calligrapher's details to `data/calligraphers.json`.
2. Run the generation script: `python3 generate_pages.py`.
3. This will create a new folder in `content/calligraphers/<slug>/`.

### Replacing Placeholder Images
- **Portrait:** Replace `static/img/placeholder-portrait.jpg` or add a specific image to the calligrapher's bundle at `content/calligraphers/<slug>/portrait.jpg` and update the template.
- **Artwork:** Replace `static/img/placeholder-work.jpg` or add specific images to the calligrapher's bundle.

### Changing the Featured List
The featured list is controlled by the `featured: true` flag in the front matter of the calligrapher's markdown file (or in `data/calligraphers.json` before running the script).

### Changing Formspree Endpoint
Update the `formspree_endpoint` in `config.toml`.

## Build Process
1. Build the Hugo site: `hugo`
2. Index for search: `pagefind --site public`
3. Deploy the `public` folder to Cloudflare Pages.
