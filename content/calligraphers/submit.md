---
title: "Suggest a Calligrapher"
description: "Help us grow the directory by suggesting a UAE-based Arabic calligrapher."
---

Know a talented calligrapher based in the UAE? Let us know!

<form action="https://formspree.io/f/mnjnnzov" method="POST">
    <div class="form-group">
        <label for="artist_name">Artist Name (Required)</label>
        <input type="text" id="artist_name" name="artist_name" required>
    </div>
    <div class="form-group">
        <label for="emirate">Emirate/City (Required)</label>
        <input type="text" id="emirate" name="emirate" required>
    </div>
    <div class="form-group">
        <label for="contact_link">Website or Contact Link (Required)</label>
        <input type="url" id="contact_link" name="contact_link" required>
    </div>
    <div class="form-group">
        <label for="specialty">Specialty Type (Required)</label>
        <select id="specialty" name="specialty" required>
            <option value="">Select a specialty</option>
            <option value="Classical">Classical</option>
            <option value="Contemporary">Contemporary</option>
            <option value="Digital">Digital</option>
            <option value="Sculptural">Sculptural</option>
        </select>
    </div>
    <div class="form-group">
        <label for="scripts">Scripts Tags (Optional)</label>
        <input type="text" id="scripts" name="scripts" placeholder="e.g., Thuluth, Naskh, Kufic">
    </div>
    <div class="form-group">
        <label for="your_name">Your Name (Required)</label>
        <input type="text" id="your_name" name="your_name" required>
    </div>
    <div class="form-group">
        <label for="your_email">Your Email (Required)</label>
        <input type="email" id="your_email" name="your_email" required>
    </div>
    <div class="form-group">
        <label for="notes">Notes (Optional)</label>
        <textarea id="notes" name="notes" rows="3"></textarea>
    </div>
    <input type="text" name="_gotcha" class="honeypot">
    <input type="hidden" name="_next" value="/thanks/">
    <button type="submit" class="btn btn-primary">Submit Suggestion</button>
</form>
