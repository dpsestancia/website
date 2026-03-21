# 🎵 Audio Playback System - Quick Reference

## How It Works

The Listen page dynamically loads audio from a CSV file and creates HTML5 audio players automatically.

## File Requirements

### 1. Audio Files (MP3)
Place your audio files in organized folders:
```
audio/
  ├── pradosham/       # Pradosham parayanam recordings
  ├── sankatahara/     # Sankatahara Chaturthi recordings  
  └── daily/           # Daily prayers and stotrams
```

**Recommended specs:**
- Format: MP3
- Bitrate: 128-192 kbps
- Sample Rate: 44.1 kHz
- File size: Under 10MB per file

### 2. CSV Manifest (`data/audio_manifest.csv`)

The CSV file tells the website which audio files to display and how to organize them.

**CSV Format:**
```csv
Category,Title,Filename,Duration,Language,Description
Pradosham,Shiva Ashtottara,audio/pradosham/shiva_ashtottara.mp3,8:45,Sanskrit,108 names of Lord Shiva
```

**Column Descriptions:**
- **Category:** `Pradosham`, `Sankatahara`, or `Daily` (case-insensitive)
- **Title:** Display name for the audio
- **Filename:** Path to MP3 file (relative to website root)
- **Duration:** Length in MM:SS format (e.g., `8:45` or `15:30`)
- **Language:** Sanskrit, Tamil, Telugu, etc.
- **Description:** Brief explanation of the recitation

## Adding New Audio

### Method 1: Local Files (Recommended for GitHub Pages)

1. **Add audio file:**
   ```bash
   cp my-recording.mp3 audio/pradosham/
   ```

2. **Update CSV:**
   ```bash
   echo "Pradosham,My Recording,audio/pradosham/my-recording.mp3,12:30,Sanskrit,Description here" >> data/audio_manifest.csv
   ```

3. **Commit and push:**
   ```bash
   git add audio/ data/audio_manifest.csv
   git commit -m "Add new audio recording"
   git push
   ```

### Method 2: Google Drive (For Large Files)

If your audio files are too large for GitHub (>100MB):

1. **Upload to Google Drive** (make publicly accessible)

2. **Get direct download link:**
   - Share link: `https://drive.google.com/file/d/FILE_ID/view`
   - Convert to: `https://drive.google.com/uc?export=download&id=FILE_ID`

3. **Add to CSV with Google Drive URL:**
   ```csv
   Pradosham,Long Recording,https://drive.google.com/uc?export=download&id=YOUR_FILE_ID,45:20,Sanskrit,Extended recitation
   ```

## Testing

### Local Testing
You **must** use a web server to test locally (CSV files won't load with `file://` protocol):

```bash
# Python 3
python -m http.server 8000

# Python 2  
python -m SimpleHTTPServer 8000

# Node.js (npx)
npx serve

# PHP
php -S localhost:8000
```

Then visit: `http://localhost:8000`

### Production Testing
After pushing to GitHub, visit your GitHub Pages URL and navigate to the LISTEN section.

## Audio Player Features

Each audio entry displays:
- ▶️ **Play/Pause button**
- ⏩ **Seek bar** - Click to jump to any position
- 🔊 **Volume control**
- 📥 **Download button** - Right-click to save MP3
- 🕒 **Duration display**
- 🌏 **Language indicator**
- 📝 **Description text**

## Troubleshooting

### "Coming Soon" message shows even with CSV file
- **Cause:** CSV file doesn't exist or has wrong name
- **Fix:** Ensure `data/audio_manifest.csv` exists and is committed to repository

### Audio players don't appear
- **Cause:** CSV rows may be malformed or Category field is incorrect
- **Fix:** Check CSV format matches column structure exactly
- **Fix:** Ensure Category is one of: `Pradosham`, `Sankatahara`, or `Daily`

### "Network error" when playing audio
- **Cause:** Audio file path in CSV is incorrect
- **Fix:** Verify Filename column path matches actual file location
- **Example:** If file is at `audio/pradosham/shiva.mp3`, CSV should have `audio/pradosham/shiva.mp3`

### Audio doesn't play on mobile
- **Cause:** File format or codec not supported
- **Fix:** Re-encode to MP3 128kbps 44.1kHz (most compatible format)
- **Fix:** Reduce file size (mobile networks may timeout on large files)

### Google Drive audio doesn't play
- **Cause:** Wrong sharing link format
- **Fix:** Convert share link to direct download link format:
  - ❌ Wrong: `https://drive.google.com/file/d/ID/view`
  - ✅ Correct: `https://drive.google.com/uc?export=download&id=ID`

## Sample CSV

```csv
Category,Title,Filename,Duration,Language,Description
Pradosham,Shiva Ashtottara Shatanama Stotram,audio/pradosham/shiva_ashtottara.mp3,8:45,Sanskrit,Recitation of Lord Shiva's 108 sacred names chanted during Pradosham
Pradosham,Rudram Chamakam,audio/pradosham/rudram_chamakam.mp3,15:30,Sanskrit,Complete Rudram and Chamakam from Krishna Yajur Veda
Sankatahara,Ganapathi Atharvashirsha,audio/sankatahara/ganapathi_atharvashirsha.mp3,12:15,Sanskrit,Sacred Upanishad dedicated to Lord Ganesha
Daily,Vishnu Sahasranamam,audio/daily/vishnu_sahasranamam.mp3,25:00,Sanskrit,Lord Vishnu's 1000 divine names for daily recitation
```

## Technical Details

### JavaScript Implementation
- **Location:** Bottom of `index.html` (vanilla JS) and within React component in `new_index.html`
- **Function:** `loadAudioLibrary()` - Fetches CSV, parses with Papa Parse, renders audio players
- **Lazy Loading:** Audio players only load when Listen tab is clicked (not on page load)
- **Error Handling:** Shows "Coming Soon" if CSV missing; gracefully handles malformed rows

### Browser Compatibility
- **Desktop:** Chrome, Firefox, Safari, Edge (all modern versions)
- **Mobile:** iOS Safari, Chrome Android, Samsung Internet
- **HTML5 Audio:** Supported by 98%+ of web browsers
- **CSV Parsing:** Uses Papa Parse library (automatically included)

### Performance
- **No impact on page load** - Audio library loads on-demand
- **Preload strategy:** `metadata` only (not full audio)
- **Bandwidth:** Audio streams on-demand, not downloaded upfront

## Advanced: Hosting Options

1. **GitHub Pages** (Current)
   - ✅ Free
   - ✅ Easy
   - ❌ 100MB file size limit
   - ❌ 1GB total repo size soft limit

2. **Google Drive**
   - ✅ Unlimited storage
   - ✅ Free for personal use
   - ⚠️ May have rate limits for heavy traffic

3. **Archive.org**
   - ✅ Unlimited free hosting
   - ✅ Permanent, no rate limits
   - ✅ Great for cultural/spiritual content
   - ⚠️ Upload review process

4. **SoundCloud**
   - ✅ Built for audio
   - ✅ Embeddable players
   - ❌ 3 hour total limit (free plan)

5. **YouTube**
   - ✅ Unlimited storage
   - ✅ Good for long recordings
   - ⚠️ Requires video (use static image)

## Support

For technical issues with the audio system:
1. Check [AUDIO-SETUP-GUIDE.md](AUDIO-SETUP-GUIDE.md) for detailed setup instructions
2. Review browser console for JavaScript errors (F12 → Console tab)
3. Verify CSV format matches column structure exactly
4. Test audio files play correctly outside the website

For recording/audio quality:
1. See [AUDIO-SETUP-GUIDE.md](AUDIO-SETUP-GUIDE.md) - "Recording Best Practices" section
2. Use Audacity (free) for editing/normalizing audio
3. Export as MP3, 128-192 kbps, mono or stereo

---

**Last Updated:** Based on Phase 1 implementation (Educational content + Audio system)
