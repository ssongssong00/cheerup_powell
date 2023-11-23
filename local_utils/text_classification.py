import openai
import requests 
import json
import config

def transcribe_audio(file_path):
    url = "https://transcribe.whisperapi.com"
    headers = {
        'Authorization': config.stt_api_key
    }
    
    # Open the audio file in binary mode
    file = {'file': open(file_path, 'rb')}
    
    data = {
        "fileType": "wav",  # default is wav
        "diarization": "false",
        "numSpeakers": "1",
        "initialPrompt": "",
        "language": "en",
        "task": "transcribe",
        "callbackURL": ""
    }
    
    response = requests.post(url, headers=headers, files=file, data=data)
    json_response = response.json()
    
    # Extracted text from the response
    extracted_text = json_response.get('text', '')
    
    return extracted_text

def chatgpt_fine_tuning():
    jsonl_data = [
        {"messages": [
            {"role": "system", "content": "As a economist, your task is to analyze the FED's monetary policy stance at the FOMC press conference. I'll give you the paragraph that the Fed Chairman said. Then you have to do the three tasks below. First, understand the context of paragraphs in the statement provided. Second, contextually, each sentence should be categorized into one of five categories: dovish, neutral, mostly hawkish, or hawkish. Third, you need to explain why you categorized the statement into a specific category."},
            {"role": "assistant", "content":"Understood. I will analyze the statement as per the instructions."}
        ]},
        {"messages": [
            {"role": "system", "content": "In light of the uncertainties and risks, and how far we have come, the Committee is proceeding carefully"},
            {"role": "assistant", "content": "Stance: Mostly dovish , Interpretation: The phrase 'proceeding carefully' reflects a cautious approach in policy-making. This suggests a balance between maintaining a hawkish bias and acknowledging potential economic slowdowns, which might preclude further interest rate hikes. The emphasis is on careful decision-making considering current economic uncertainties and risks."}
        ]},
        {"messages": [
            {"role": "system", "content": "We have asset purchases, and we’ve now said that we won’t go any lower than this, and—but—but that we’re prepared to adjust as appropriate, and rates are at the effective lower bound."},
            {"role": "assistant", "content": "Stance: dovish , Interpretation: The reference to 'asset purchases' and 'we won’t go any lower than this' indicates a robust intention to maintain the current asset purchase levels. The term 'rates are at the effective lower bound' signifies that rates are already at a significantly low level, implying no further rate reductions are currently under consideration."}
        ]},
        {"messages": [
            {"role": "system", "content": "Economic activity remained resilient, job creation remains strong while cooling a bit, and the June CPI report actually came in a bit better than expectations for a change. And the June CPI report, of course, was welcomed, but it’s only one report, one month’s data. We hope that inflation will follow a lower path, as was—that will be consistent with the CPI reading, but we don’t know that, and we’re just going to need to see more data."}, 
            {"role": "assistant", "content":  "Stance: Dovish , Interpretation: The acknowledgment of resilient economic activity and the better-than-expected June CPI report suggests an optimistic outlook, aligning with a dovish stance. Chairman Powell's comments during the press conference that the decision for additional rate hikes depends on further data and his favorable view of the June CPI report further support a dovish interpretation. This implies a cautious approach to policy tightening, waiting for more data to confirm the inflation trend."}
        ]},
        {"messages": [
            {"role": "system", "content": "Nominal wage growth has shown signs of easing, and job vacancies have declined so far this year. While the jobs-to-workers gap has declined, labor demand still substantially exceeds the supply of available workers."}, 
            {"role": "assistant", "content":  "Stance: Mostly Dovish , Interpretation: This statement notes a slight easing in the labor market. Chairman Powell's remarks about the labor market showing signs of easing, suggest a slightly dovish stance compared to previous more assertive statements about the tightness of the labor market. This indicates a recognition of potential changes in labor market dynamics, which might influence future policy decisions."}
        ]},
        {"messages": [
            {"role": "system", "content": "In light of the cumulative tightening of monetary policy and the lags with which monetary policy affects economic activity and inflation, the Committee decided to raise interest rates by 50 basis points today, a step-down from the 75 basis point pace seen over the previous four meetings."}, 
            {"role": "assistant", "content":  "Stance: Dovish , Interpretation: The shift from a 75 basis point increase to a more moderate 50 basis point rise, despite ongoing high inflation risks, indicates a cautious approach and a potential pivot towards less aggressive monetary tightening. This moderation, especially considering Chairman Powell's earlier exclusion of a 75 basis point hike possibility, can be interpreted as a dovish signal amidst the prevailing inflation concerns. It suggests a balancing act between managing inflation and not over-tightening in a way that could significantly dampen economic activity."}
        ]},
        {"messages": [
            {"role": "system", "content": "In determining the extent of additional policy firming that may be appropriate to return inflation to 2 percent over time, the Committee will take into account the cumulative tightening of monetary policy, the lags with which monetary policy affects economic activity and inflation, and economic and financial developments."}, 
            {"role": "assistant", "content":  "Stance: Mostly hawkish , Interpretation: This sentence means continued openness to policy tightening to curb inflation, but a cautious approach that takes into account the cumulative impact of previous policies and economic development. This refers to most hawkish positions with a subtle perspective on future policy actions."}
        ]},
        {"messages": [
            {"role": "system", "content": "In light of how far we’ve come in tightening policy, the uncertain lags with which monetary policy affects the economy, and potential headwinds from credit tightening, the Committee decided at today’s meeting to maintain the target range for the federal funds rate at 5 to 5¼ percent and to continue the process of significantly reducing our securities holdings."}, 
            {"role": "assistant", "content":  "Stance: Hawkish , Interpretation: Despite maintaining the current federal funds rate, the emphasis on the progress in tightening policy and the continuation of reducing securities holdings indicates a hawkish stance. The decision reflects an acknowledgment of the impacts of previous policy decisions and a readiness to possibly increase rates in the future."}
        ]},
        {"messages": [
            {"role": "system", "content": "In determining the extent of additional policy firming that may be appropriate to return inflation to 2 percent over time, the Committee will take into account the cumulative tightening of monetary policy, the lags with which monetary policy affects economic activity and inflation, and economic and financial developments."}, 
            {"role": "assistant", "content":  "Stance: mostly hawkish , Interpretation: The mention of 'additional policy firming' strongly suggests a possibility of rate hikes. This underscores a careful consideration to bring inflation back sustainably to the 2 percent target."}
        ]},
        {"messages": [
            {"role": "system", "content": "As shown in the SEP, the median projection for the appropriate level of the federal funds rate is 4.4 percent at the end of this year, 1 percentage point higher than projected in June."}, 
            {"role": "assistant", "content": "Stance: Hawkish , Interpretation: The mention of 'additional policy firming' strongly suggests a possibility of rate hikes. This underscores a careful consideration to bring inflation back sustainably to the 2 percent target."}
        ]},
        {"messages": [
            {"role": "system", "content": "All FOMC participants forecast that this remaining test will be met next year. The median projection for the appropriate level of the federal funds rate is 0.9 percent at the end of 2022, about ½ percentage point higher than projected in September."}, 
            {"role": "assistant", "content":  "Stance: Hawkish , Interpretation: The median projection for the federal funds rate being adjusted upwards by 0.5 percentage points compared to previous projections in September indicates a shift towards more aggressive monetary tightening. This significant upward adjustment in the rate forecast, along with the consensus on meeting future criteria, points to a proactive and assertive approach to managing inflation and economic growth."}
        ]}
    ]

    # 파일에 JSON Lines 형식으로 저장
    with open('make_jsonl.jsonl', 'w') as file:
        for entry in jsonl_data:
            json_line = json.dumps(entry)  # 딕셔너리를 JSON 문자열로 변환
            file.write(json_line + '\n')  # 파일에 JSON 문자열과 줄바꿈 추가

    with open("make_jsonl.jsonl") as f: 
        for line in f: print(line)

    
    openai.api_key= config.gpt_api_key
    
    training_response=openai.File.create(
            file=open("make_jsonl.jsonl","rb"),
            purpose='fine-tune'
    )
    
    training_file_id = training_response["id"]
    
    print ("Training file id:",training_file_id)

    id="file-umorJCarC7TYCczQ8TAbkL4d"
    
    response = openai.FineTuningJob.create(
    training_file=id,
    model="gpt-3.5-turbo"
    )
    
    job_id=response["id"]
    print(response)
    

# 분석 함수 정의
def analyze_fed_statement(st1):
    openai.api_key= config.gpt_api_key

    completion = openai.ChatCompletion.create(
        model="ft:gpt-3.5-turbo-0613:personal::8NkY7Btw",
        messages=[
            {"role": "system", "content": "As an economist, your task is to analyze the FED's monetary policy stance at the FOMC press conference based on the given paragraph. Consider the overall context and tone of the paragraph to categorize it into one of the following categories: dovish, neutral, mostly hawkish, or hawkish. Then, pexplain why you categorized the statement into a specific category for your categorization, focusing on the paragraph as a whole rather than analyzing each sentence separately. In other words, you can say 'stance' and 'interpretation'. Here's the text I'm providing."},
            {"role": "user", "content": f"Analyze this statement: {st1}"}
        ],
        temperature=0,
        max_tokens=250,
    )
    result = completion["choices"][0]["message"]["content"]
    stance_start = result.find('Stance:')
    interpretation_start = result.find('Interpretation:')
    
    # Extract Stance
    if stance_start != -1:
        stance_end = result.find(',', stance_start)
        stance = result[stance_start + len('Stance:'):stance_end].strip()
    else:
        stance = None
    
    # Extract Interpretation
    if interpretation_start != -1:
        interpretation = result[interpretation_start + len('Interpretation:'):].strip()
    else:
        interpretation = None

    return stance, interpretation