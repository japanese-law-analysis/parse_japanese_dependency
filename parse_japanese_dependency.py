import spacy
import ginza
import json
import argparse


def parse_document(sentence, nlp):
    doc = nlp(sentence)
    token_info = {}
    len_sum = 0
    for sent in doc.sents:
        for token in sent:
            i = str(token.i)
            token_len = len(token.text)
            token_info[i] = { "start":len_sum, "end": len_sum + token_len - 1, "text": token.text }
            len_sum = len_sum + token_len

    # 係受けの情報を追加する
    for span in ginza.bunsetu_spans(doc):
        for token in span.lefts:
            i = str(token.i)
            d = token_info[i]
            d["head_start"] = span.start
            d["head_end"] = span.end
            token_info[i] = d
    return token_info

parser = argparse.ArgumentParser(prog = "parse japanese dependency", description = "係り受け解析")
parser.add_argument("-i", "--input")
parser.add_argument("-o", "--output")
parser.add_argument("-j", "--json")
parser.add_argument("-e", "--electra", action="store_true")
parser.add_argument("-n", "--normal", action="store_true")


if __name__ == "__main__":
    args = parser.parse_args()
    input_file_name = args.input
    output_file_name = args.output
    if input_file_name == None:
        input_data = json.loads(args.json)
    else:
        input_f = open(input_file_name, "r", encoding="UTF-8")
        input_s = input_f.read()
        input_f.close()
        input_data = json.loads(input_s)
    if args.electra == True:
        nlp = spacy.load("ja_ginza_electra")
    elif args.normal == True:
        nlp = spacy.load("ja_ginza")
    else:
        # default
        nlp = spacy.load("ja_ginza_electra")
    output_s = "{"
    is_head = True
    for k,v in input_data.items():
        d = parse_document(v, nlp)
        if is_head:
            output_s = output_s + "\n"
            is_head = False
        else:
            output_s = output_s + ",\n"
        s = json.dumps(d, ensure_ascii=False)
        output_s = output_s + f"\"{k}\":{s}"
    output_s = output_s + "\n}"
    if output_file_name == None:
        print(output_s)
    else:
        output_f = open(output_file_name, "w", encoding="UTF-8")
        output_f.write(output_s)
        output_f.close()


