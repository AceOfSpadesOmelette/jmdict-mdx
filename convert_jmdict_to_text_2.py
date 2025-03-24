import json

def convert_entry_to_html(entry, tags):
    html_entries = []
    
    # Combine kanji and kana for processing
    kanji_items = entry.get('kanji', [])
    kana_items = entry.get('kana', [])
    entry_id = entry.get('id')
    
    print(entry_id)
    
    # Process each kanji and kana
    items = kanji_items + kana_items
    for item in items:
        # Display the text of the current kanji/kana before the entry
        item_text = item.get("text")
        html = f'{item_text}\n<div class="jmdict-entry" style="line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 20px;"><div class="jmdict-entry-name" style="font-size: 24px;">{item_text}</div>'
        
        # Create entry header with all kanji and kana
        header_html = '<div class="entry-header" style="border-bottom: 2px solid #eee; padding-bottom: 10px; margin-bottom: 20px;">'
        
        # Kanji row
        if kanji_items:
            header_html += '<div class="jmdict-kanji-row">'
            kanji_texts = [kanji.get("text") for kanji in kanji_items]
            header_html += '・'.join([f'<span class="kanji" style="font-size: 18px;">{kanji}</span>' for kanji in kanji_texts])
            header_html += '</div>'  # Close kanji row
        
        # Kana row
        if kana_items:
            header_html += '<div class="jmdict-kana-row">【'
            kana_texts = [kana.get("text") for kana in kana_items]
            header_html += '・'.join([f'<span class="kana" style="font-size: 18px;">{kana}</span>' for kana in kana_texts])
            header_html += '】</div>'  # Close kana row

        header_html += '</div>'  # Close entry-header
        
        # Add the header to the entry
        html += header_html
        
        # Process senses (only include the first sense for each entry)
        for idx, sense in enumerate(entry.get('sense', []), start=1):
            html += f'<div class="sense" style="margin-bottom: 20px; padding-left: 20px;"><strong>{idx}</strong>'
            
            # Part of speech
            pos_tags = [f'<span class="pos-tag" style="padding: 2px 6px; border-radius: 3px; margin-right: 5px;">[{pos}]</span>' for pos in sense.get('partOfSpeech', [])]
            html += ' <span class="jmdict-pos" style="font-size: 0.9em; margin-bottom: 5px;">' + ' '.join(pos_tags) + '</span>'
            
            # Glosses
            glosses = [g['text'] for g in sense.get('gloss', []) if g['lang'] == 'eng']
            html += ' <div class="glosses" style="margin-bottom: 10px;">' + ', '.join(glosses) + '</div>'
            
            # Related section
            if 'related' in sense:
                related_list = []
                for related in sense['related']:
                    if len(related) > 1:
                        related_list.append(f'See also {related[0]}, def {related[1]}.')
                    else:
                        related_list.append(f'See also {related[0]}.')
                if related_list:
                    html += ' <div class="jmdict-related" style="font-size: 14px; font-style: italic; margin: 5px 0;">' + ' '.join(related_list) + '</div>'
            
            # Info section
            info_list = []
            if 'info' in sense:
                info_list = [info for info in sense.get('info', [])]
            if info_list:
                html += ' <div class="jmdict-info" style="font-size: 14px; font-style: italic; margin: 5px 0;">' + ', '.join(info_list) + '</div>'
            
            # Misc section using tags
            misc_list = []
            if 'misc' in sense:
                for tag in sense['misc']:
                    if tag in tags:
                        misc_list.append(tags[tag])
            if misc_list:
                html += ' <div class="jmdict-misc" style="font-size: 14px; font-style: italic; margin: 5px 0;">' + ', '.join(misc_list) + '</div>'
            
            # Applies to Kanji section
            applies_to_kanji = sense.get('appliesToKanji', [])
            if applies_to_kanji != ['*'] and applies_to_kanji:
                html += f' <div class="jmdict-appliesToKanji" style="font-size: 14px; font-style: italic; margin: 5px 0;">Only applies to {", ".join(applies_to_kanji)}.</div>'
            
            # Example sentences
            if 'examples' in sense:
                for example in sense['examples']:
                    for sentence in example.get('sentences', []):
                        if 'land' in sentence and sentence['land'] == 'jpn':
                            html += f' <div class="jmdict-example" style="border-left: 4px solid; padding: 10px; margin: 10px 0; border-radius: 4px;"><div class="example-jpn" font-size: 16px; margin-bottom: 5px;">{sentence["text"]}</div>'
                        if 'land' in sentence and sentence['land'] == 'eng':
                            html += f' <div class="example-eng">{sentence["text"]}</div></div>'
            
            html += ' </div>'  # Close sense div
        
        html += ' </div>'  # Close jmdict-entry div
        html_entries.append(html + '\n</>\n')  # Add the ending tag

    return ''.join(html_entries)  # Join all entries together

def main():
    input_file = 'jmdict-examples-eng-3.6.1.json'
    output_file = 'jmdict-examples-eng-3.6.1.txt'

    # Read JSON data
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Prepare to write HTML entries
    html_entries = []
    tags = data.get('tags', {})  # Get the tags from the JSON data
    for entry in data.get('words', []):  # Process only the first 100 entries
        html_entry = convert_entry_to_html(entry, tags)
        html_entries.append(html_entry)

    # Write to output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(html_entries)

if __name__ == '__main__':
    main()