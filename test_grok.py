from src.caption_generator import CaptionGenerator

# Test the Grok-powered caption generator
generator = CaptionGenerator()

print("🧪 Testing Grok Caption Generator...\n")

test_transcript = "Player gets an insane ace in Rainbow Six Siege, one tap headshot on the last enemy"

captions = generator.generate_hype_captions(test_transcript)

print("🎥 Generated Captions for TikTok Shorts:")
for i, caption in enumerate(captions, 1):
    print(f"{i}. {caption}")
