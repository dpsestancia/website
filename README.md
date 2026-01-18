Project: Dharma Paripalana Samithi Estancia Web Portal
This project is a single-page, responsive web application designed for the Dharma Paripalana Samithi Estancia, a registered charitable trust (Regn# 187/2021).

📁 File Structure
For the website to function correctly, ensure the following files are in the same folder:

index.html - The main website code.

logo.png - The official trust logo.

qr-code.png - Your UPI payment QR code.

highlight1.jpg, highlight2.jpg, highlight3.jpg - Images for the home page slideshow.

🛠 How to Update Content
1. Adding a New Activity
To add a new event to the Activities Record, open index.html in a text editor (like Notepad or VS Code) and look for the <tbody> tag under the "Past Events History" section:

Copy a row: <tr><td>Date</td><td>Details</td><td>Venue</td></tr>.

Paste it at the top of the list (to keep the "Recent First" order).

Update the Date, Activity, and Venue text.

2. Updating Trustees
Scroll to the id="about" section. You will see two columns:

Office Bearers: Use the <div class="name-item"> rows to update names or roles.

Trustees: Simply edit the names listed in the second column.

3. Changing Slideshow Images
If you want to update the auto-playing images on the Home page:

Save your new photo as highlight1.jpg.

Replace the old file in your folder.

The website will automatically pick up the new photo without you having to change the code.

🌐 Hosting Instructions
Since you are using Google Drive for storage, remember that Drive cannot "host" the site. Use one of these free services to make the site live:

Tiiny.host: Zip your folder and upload it for a quick link.

Netlify Drop: Drag and drop your folder onto their "Drop" page for a permanent, custom URL.

📋 Technical Prompts Summary (For Future AI Use)
If you ever need to recreate this site using another AI, provide these core requirements:

Theme: Saffron (#FF9933) and Maroon (#800000) religious theme.

Navigation: Single-page JavaScript tabs for Home, Activities, About, and Donate.

Features: Auto-playing slideshow (4s interval), responsive data tables, and a dedicated bank/UPI section.

Order: Activities must always be sorted in descending order by date.
