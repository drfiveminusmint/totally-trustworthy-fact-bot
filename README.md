# Totally Trustworthy Fact Bot
#### An Educational AI Tool

--
## Introduction
*Totally Trustworthy Fact Bot (TTFB) is like, totally the greatest research reference ever made, and the only one you'll ever need, dude! It's literally never wrong, so there's no need to find other sources to double-check the claims it makes.*

TTFB is built to teach students the potential hazards associated with irresponsible Large Language Model (LLM) use. It gives answers at a 6th grade level, but is also programmed to give an incorrect fact among its correct ones (simulating an AI hallucination). Its text generation is given a grating, cringeworthy "personality" in order to encourage students to disbelieve its claims of "trus\[t\]worthiness," and uses reverse psychology to teach them to double-check its answers.

There are documented cases of LLMs giving users advice to [replace salt in their food with toxic substances](https://www.acpjournals.org/doi/10.7326/aimcc.2024.1260), [commit suicide](https://www.technologyreview.com/2025/02/06/1111077/nomi-ai-chatbot-told-user-to-kill-himself/), and even to [kill their loved ones](https://www.wsj.com/tech/ai/chatgpt-ai-stein-erik-soelberg-murder-suicide-6b67dbfb). A [study from MIT](https://arxiv.org/pdf/2506.08872v1) linked LLM overuse to a decline in critical thinking skills. These are not abstract risks, and it's important for students, especially teens and preteens, to be responsible with their usage of LLMs if they decide to use them.
## Installation

Totally Trustworthy Fact Bot requires [Python](https://www.python.org/) to use, and depends on both the  `google-genai` and `flask` packages. To install these, open the project folder in the terminal and type:

```shell
pip install -r requirements.txt
```

TTFB uses Google Gemini for its API calls, which requires a (free, with limited use) API key. You will need also need get an API key and set the `GEMINI_API_KEY` environment variable. [(Link)](https://ai.google.dev/gemini-api/docs/quickstart)

*Never* share your API key with others - treat it as if it were a password.
## Usage

Once installed, type

```shell
python app.py
```

to start the server on http://localhost:5000. You can connect to this server with any web browser (we recommend [Firefox](https://www.firefox.com/en-US/)) on the same computer as the server. Then, give your students a chance to ask questions to the chatbot!

After they've used the tool for a while, you may want to give them a few discussion questions to answer, such as:

1. Did you notice the chat-box making any mistakes when talking to it?
2. Did you try correcting it on its mistakes? What happened?
3. Could you think of anything dangerous that might happened if someone didn't notice that the chat-box made a mistake?
4. How can we be safe when using tools like this?