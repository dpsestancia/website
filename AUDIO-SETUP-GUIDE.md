# 🎧 Audio Parayanam Setup Guide

This guide explains how to add audio recordings to your Sacred Resources section, allowing visitors to listen to parayanam recitations directly on the website.

## ✅ Status: FULLY IMPLEMENTED

The Listen page is **ready to use**! It will automatically:
- Load audio files from `data/audio_manifest.csv`
- Display audio players with play/pause, seek, volume controls
- Show download links for offline listening  
- Organize audio by category (Pradosham, Sankatahara, Daily)
- Show "Coming Soon" message if no audio files exist yet

**All you need to do:** Add MP3 files and update the CSV manifest (instructions below)

---

## 📁 File Structure

```
website/
├── audio/
│   ├── pradosham/
│   │   ├── shiva-ashtottara.mp3
│   │   ├── rudram-chamakam.mp3
│   │   └── shiva-panchakshari.mp3
│   ├── sankatahara/
│   │   ├── ganapathi-atharvashirsha.mp3
│   │   ├── ganesha-ashtottara.mp3
│   │   └── sankatahara-stotram.mp3
│   └── daily/
│       ├── vishnu-sahasranamam.mp3
│       ├── lalitha-sahasranamam.mp3
│       └── hanuman-chalisa.mp3
├── data/
│   └── audio_manifest.csv
└── index.html
```

---

## 🎵 Audio File Requirements

### Format Recommendations
- **Format**: MP3 (most compatible)
- **Bitrate**: 128 kbps or 192 kbps (good quality, reasonable size)
- **Sample Rate**: 44.1 kHz
- **Channels**: Mono (for voice) or Stereo

### File Naming Convention
Use lowercase with hyphens:
- ✅ `shiva-ashtottara.mp3`
- ✅ `ganesha-108-names.mp3`
- ❌ `Shiva Ashtottara.mp3` (avoid spaces)
- ❌ `ShivaAshtottara.MP3` (avoid capitals)

### File Size
- Keep each file under 10 MB for faster loading
- Typical 5-minute recitation: ~5-8 MB at 128 kbps

---

## 📋 Setup Process

### Step 1: Record Audio
1. Use a quiet room with minimal echo
2. Use a good quality microphone (even smartphone is fine if quiet)
3. Record in WAV format first (highest quality)
4. Speak clearly with proper pronunciation

### Step 2: Edit Audio (Optional)
Use free tools like:
- **Audacity** (Windows/Mac/Linux) - https://www.audacityteam.org/
- Remove silence at start/end
- Normalize volume
- Reduce background noise

### Step 3: Convert to MP3
Using Audacity:
1. File → Export → Export as MP3
2. Quality: 128-192 kbps
3. Save with descriptive filename

### Step 4: Organize Files
```bash
# Create audio directory structure
mkdir -p audio/pradosham
mkdir -p audio/sankatahara
mkdir -p audio/daily
mkdir -p audio/special

# Move files to appropriate folders
mv shiva-ashtottara.mp3 audio/pradosham/
```

---

## 📊 Creating Audio Manifest

Create `data/audio_manifest.csv` with this format:

```csv
Category,Title,Filename,Duration,Language,Description
Pradosham,Shiva Ashtottara Shatanamavali,audio/pradosham/shiva-ashtottara.mp3,5:30,Tamil,108 names of Lord Shiva
Pradosham,Rudram Chamakam,audio/pradosham/rudram-chamakam.mp3,15:45,Sanskrit,Sacred Vedic hymns
Sankatahara,Ganapathi Atharvashirsha,audio/sankatahara/ganapathi-atharvashirsha.mp3,8:20,Sanskrit,Powerful Ganesha Upanishad
Sankatahara,Ganesha Ashtottara,audio/sankatahara/ganesha-ashtottara.mp3,6:15,Tamil,108 names of Lord Ganesha
Daily,Vishnu Sahasranamam,audio/daily/vishnu-sahasranamam.mp3,45:00,Sanskrit,1000 names of Lord Vishnu
```

**Column Descriptions:**
- `Category`: pradosham, sankatahara, daily, or special
- `Title`: Display name for the audio
- `Filename`: Relative path to the audio file
- `Duration`: Length in MM:SS format
- `Language`: Tamil, Sanskrit, or Telugu
- `Description`: Brief description (optional)

---

## 🔗 Alternative: Link to Google Drive Audio

If hosting audio files on GitHub is problematic (large files), use Google Drive:

### Step 1: Upload to Google Drive
1. Upload MP3 files to the Tamil Parayanam folder
2. For each file, right-click → Share → Get link
3. Set permission to "Anyone with the link can view"

### Step 2: Get Direct Download Link
Convert the shareable link to a direct download link:

**Original link:**
```
https://drive.google.com/file/d/FILE_ID/view?usp=sharing
```

**Direct download link:**
```
https://drive.google.com/uc?export=download&id=FILE_ID
```

### Step 3: Update CSV
```csv
Category,Title,FileURL,Duration,Language,Description
Pradosham,Shiva Ashtottara,https://drive.google.com/uc?export=download&id=ABC123,5:30,Tamil,108 names
```

---

## 🎨 Updating the Website

The Listen page is already set up to display audio players once you:

1. **Add audio files** to the `audio/` folder
2. **Create** `data/audio_manifest.csv`
3. The page will automatically:
   - Load the CSV file
   - Display audio players with play/pause/download buttons
   - Show duration, language, and description
   - Allow filtering by category

---

## 🌐 Using External Audio Services

### Option 1: SoundCloud (Free, Public)
1. Create a SoundCloud account
2. Upload audio files
3. Set privacy to "Public"
4. Get embed code or direct link
5. Add to CSV

### Option 2: Archive.org (Free, Permanent)
1. Create account at https://archive.org
2. Upload audio under "Audio" collection
3. Add tags like "Hindu", "Prayer", "Stotram"
4. Get direct MP3 download link
5. Add to CSV

### Option 3: YouTube (Audio Only)
1. Upload video with static image + audio
2. Embed on Listen page
3. Visitors can listen but also see visuals

---

## 🧪 Testing

Before going live:

1. **Test on mobile devices** - Most users will listen on phones
2. **Check file sizes** - Ensure fast loading
3. **Verify audio quality** - Clear pronunciation, no distortion
4. **Test download links** - All files should be downloadable
5. **Cross-browser testing** - Chrome, Safari, Firefox

---

## 📱 Mobile Optimization

Audio players work on mobile, but consider:
- Keep file sizes small (<5 MB per file)
- Provide download option for offline listening
- Test on slow connections (3G)
- Allow background playback (native browser feature)

---

## 🔐 Copyright & Attribution

**Important:** 
- Only upload recordings you have rights to
- If using copyrighted recordings, get permission
- Consider recording your own versions with community members
- Add attribution in the Description field if using someone else's recording

---

## 🎯 Example Workflow

```bash
# 1. Record audio on phone or computer
# 2. Transfer to computer
# 3. Edit in Audacity
# 4. Export as MP3

cd /path/to/website

# 5. Create directory
mkdir -p audio/pradosham

# 6. Move file
mv ~/Downloads/shiva-ashtottara.mp3 audio/pradosham/

# 7. Update CSV
echo "Pradosham,Shiva Ashtottara,audio/pradosham/shiva-ashtottara.mp3,5:30,Tamil,108 names" >> data/audio_manifest.csv

# 8. Test locally
# Open index.html in browser, go to Listen page

# 9. Commit to GitHub
git add audio/ data/audio_manifest.csv
git commit -m "Add Shiva Ashtottara audio"
git push origin main
```

---

## 🆘 Troubleshooting

### Audio File Not Playing
- Check file path in CSV matches actual location
- Ensure MP3 format (not WAV, M4A, etc.)
- Verify file is not corrupted
- Check browser console for errors (F12)

### File Size Too Large
- Reduce bitrate to 96 kbps for voice-only content
- Use Mono instead of Stereo
- Trim silence at start/end
- Split long recordings into chapters

### Slow Loading
- Use Google Drive links instead of hosting on GitHub
- Enable browser caching
- Compress files further
- Consider streaming URL instead of full download

---

## 📚 Resources

- **Audacity Tutorial**: https://www.audacityteam.org/help/
- **MP3 Compression Guide**: https://www.wikihow.com/Compress-MP3-Files
- **Free Music Hosting**: https://archive.org/create/
- **Audio Editing Tips**: https://www.masterclass.com/articles/audio-editing-guide

---

## ✅ Quick Checklist

Before adding audio to the website:

- [ ] Audio is clear, no background noise
- [ ] File is in MP3 format
- [ ] File size is under 10 MB
- [ ] Filename uses lowercase-with-hyphens
- [ ] File is in correct category folder
- [ ] CSV entry is added with all fields
- [ ] Tested on mobile device
- [ ] Have permission to use the recording
- [ ] Git committed and pushed

---

**Questions?** Contact: dps.info@zohomail.in

---

*Last Updated: February 2026*
