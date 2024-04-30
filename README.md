# Arxiv Librarian

> Your personal AI research assistant, making the latest in AI insights accessible.

![Arxiv Librarian](data/about/Arxiv_Librarian.png)

Dr. Alistair Grey, also known as the "Arxiv Librarian," simplifies the overwhelming world of AI research for enthusiasts and professionals. With a Ph.D. in Computer Science and extensive AI expertise, he translates complex information into clear, digestible summaries through a user-friendly platform. The Arxiv Librarian service tackles information overload with a chat interface for natural conversations, daily email summaries, and timely updates on new research, making it easier for users to stay informed and at the forefront of AI innovation. Dr. Grey's approachable and clear communication ensures that users not only stay updated but also deeply understand the latest AI advancements.

His persona can be found [here](persona.md).

---

[Assistants API Beta](https://platform.openai.com/docs/assistants/overview)

[arXiv - Computer Science - Artificial Intelligence](https://arxiv.org/list/cs.AI/recent)

## Product Definition

The Arxiv Librarian provides a personalized and streamlined approach for AI enthusiasts and software engineers to stay updated on the latest AI research. It addresses the challenge of information overload in the field, where over 87,710 articles are available in the AI category on Arxiv, with new papers added daily. This tool simplifies the task of staying informed by offering a chat interface for natural language conversations, daily email summaries, and near real-time updates of new research papers. By delivering targeted, digestible summaries, Arxiv Librarian makes it easier for professionals to navigate the vast volumes of information and stay at the forefront of AI innovation.

### Problem

Arxiv Librarian addresses the daunting challenge of information overload for AI Enthusiast Software Engineers by simplifying the discovery of relevant, impactful research in the vast, ever-growing ocean of AI publications on Arxiv. It aids users in staying current with the latest advancements, exploring specific topics of interest, and prompting exploratory queries like ‘What’s new in the world of AI?’ ensuring they remain at the forefront of AI innovation without feeling overwhelmed.

### North Star

The North Star for Arxiv Librarian is centered around the efficiency and effectiveness of user discovery and research. Specifically, measuring success through the ability of users to quickly find and discover recent AI advancements, without the need to sift through dozens of whitepapers. This can be quantified by tracking user engagement metrics such as the average time spent to find relevant research, the frequency of use, and user feedback on the relevancy and utility of the information provided. Success means users consistently find the content they need with minimal effort and high satisfaction.

### Product Vision

Arxiv Librarian envisions to transform how individuals interact with AI research. Leveraging natural language processing for personalized conversations, it aims to empower users to discover, research, and discuss the latest trends and possibilities in AI, all through an intuitive daily summary model.

### Business Case

The swift pace of AI innovation creates a unique opportunity for Arxiv Librarian to become an indispensable tool for professionals and enthusiasts alike. By offering real-time updates, personalized research insights, and discussions on the latest AI developments, it bridges the gap between the rapid advancements in the field and the lagging traditional publication process. This model not only keeps users at the cutting edge of AI but also opens revenue streams through subscriptions for premium features, partnerships with academia and industry for cutting-edge research dissemination, and targeted advertising from AI-related services and product companies aiming to reach a highly engaged audience.

### Technology

To build Arxiv Librarian’s innovative features, a robust technology stack is crucial:

- **Python**: A versatile programming language ideal for ETL processes, data analysis, and integration with AI models.
- **OpenAI Assistants**: Leverage for natural language processing and understanding, enabling the chat interface to provide intelligent, contextual responses.
- **Vector Stores**: Utilize vector databases to efficiently manage and query the vast dataset of AI research documents, enhancing the search and personalization features.

This stack not only supports the real-time, intensive data processing needs of Arxiv Librarian but also ensures scalability and flexibility for future expansion and enhancements.

### Key Features

- Chat interface for natural language queries, allowing users to effortlessly explore AI topics and research.
- Near real-time update mechanism to ingest new AI research documents from Arxiv, ensuring the latest papers are always available.
- An ETL (Extract, Transform, Load) pipeline facilitating regular data updates, keeping the content fresh and relevant.
- Daily email summaries offering concise overviews of new papers, helping users stay informed with minimal effort.

### Users

### AI Enthusiast Software Engineers

Software engineers with a keen interest in AI, seeking to stay updated with the latest research findings and discussions in the field.

## Setup

1. Clone the repository:

```bash
git clone https://github.com/DEV3L/arxiv-librarian
cd arxiv-librarian
```

2. Copy the env.local file to a new file named .env and replace `OPENAI_API_KEY` with your actual OpenAI API key:

```bash
cp env.local .env
```

3. Setup a virtual environment with dependencies and activate it:

```bash
brew install hatch
hatch env create
hatch shell
```

1. Run the main script:

```bash
python run_chat.py
```

## Testing

### Unit Tests

```bash
pytest
```

With coverage:

```bash
pytest --cov
```

With coverage for Coverage Gutters:

```bash
pytest --cov --cov-report lcov

Command + Shift + P => Coverage Gutters: Watch
```
