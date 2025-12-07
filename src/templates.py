import random
import hashlib
from datetime import datetime

# Diverse list of philosophers from different eras and traditions
PHILOSOPHERS = [
    # Ancient Western
    "Socrates", "Plato", "Aristotle", "Epicurus", "Zeno of Citium", "Marcus Aurelius",
    "Epictetus", "Seneca", "Diogenes", "Heraclitus", "Parmenides", "Pythagoras",
    
    # Eastern Philosophy
    "Confucius", "Laozi (Lao Tzu)", "Zhuangzi", "Buddha (Siddhartha Gautama)", 
    "Nagarjuna", "Shankara", "Rumi", "Al-Ghazali", "Ibn Rushd (Averroes)", "Mozi",
    
    # Medieval & Renaissance
    "Thomas Aquinas", "Augustine of Hippo", "Maimonides", "Duns Scotus", 
    "William of Ockham", "Niccolò Machiavelli", "Erasmus",
    
    # Early Modern
    "René Descartes", "Baruch Spinoza", "Gottfried Leibniz", "John Locke", 
    "David Hume", "Immanuel Kant", "George Berkeley", "Thomas Hobbes",
    
    # 19th Century
    "Georg Hegel", "Arthur Schopenhauer", "Søren Kierkegaard", "Friedrich Nietzsche",
    "Karl Marx", "John Stuart Mill", "Edmund Husserl", "William James",
    
    # 20th Century & Contemporary
    "Bertrand Russell", "Ludwig Wittgenstein", "Martin Heidegger", "Jean-Paul Sartre",
    "Simone de Beauvoir", "Albert Camus", "Hannah Arendt", "Michel Foucault",
    "Jacques Derrida", "Jürgen Habermas", "John Rawls", "Martha Nussbaum",
    "Slavoj Žižek", "Judith Butler", "Peter Singer", "Alain Badiou"
]

# Philosophical schools and movements
PHILOSOPHICAL_SCHOOLS = [
    "Stoicism", "Epicureanism", "Existentialism", "Phenomenology", "Pragmatism",
    "Rationalism", "Empiricism", "Idealism", "Materialism", "Nihilism",
    "Absurdism", "Utilitarianism", "Deontology", "Virtue Ethics", "Zen Buddhism",
    "Confucianism", "Taoism", "Skepticism", "Cynicism", "Platonism"
]

# Philosophical concepts
PHILOSOPHICAL_CONCEPTS = [
    "The Good Life", "Justice", "Truth", "Beauty", "Virtue", "Freedom",
    "Consciousness", "Identity", "Time", "Causality", "Ethics", "Morality",
    "Meaning of Life", "Death", "Suffering", "Happiness", "Wisdom",
    "Knowledge", "Reality", "Existence", "Being", "Nothingness", "Authenticity"
]


def get_seed_from_timestamp():
    """Generate a unique seed from current timestamp to ensure variety."""
    now = datetime.utcnow()
    # Create a unique seed from date + hour to get different content each run
    seed_string = f"{now.year}{now.month}{now.day}{now.hour}{now.minute}"
    return int(hashlib.md5(seed_string.encode()).hexdigest()[:8], 16)


def get_philosophical_quote_prompt() -> str:
    """Generate prompt for a philosophical quote with deep context."""
    seed = get_seed_from_timestamp()
    random.seed(seed)
    
    philosopher = random.choice(PHILOSOPHERS)
    concept = random.choice(PHILOSOPHICAL_CONCEPTS)
    
    return f"""
Generate a deep, meaningful philosophical quote from {philosopher} related to {concept}.

Format your response EXACTLY like this:

🧠 **Philosophical Quote of the Day**

💭 "{{"<The actual quote here>"}}"

— **{philosopher}**

📖 **Context & Meaning:**
<Explain the historical context of this quote, what {philosopher} meant by it, and how it relates to {concept}. Be thorough and educational - 3-4 sentences.>

🌟 **Modern Application:**
<How can we apply this wisdom in modern life? Give practical insights - 2-3 sentences.>

#Philosophy #{philosopher.replace(" ", "")} #{concept.replace(" ", "")}

IMPORTANT: 
- Use a REAL, authentic quote from {philosopher}
- Make the explanation deep and educational
- Focus on genuine philosophical insight, not generic motivation
- Be historically accurate
"""


def get_philosophical_thinking_prompt() -> str:
    """Generate prompt for explaining a philosophical concept or school of thought."""
    seed = get_seed_from_timestamp()
    random.seed(seed)
    
    school = random.choice(PHILOSOPHICAL_SCHOOLS)
    
    return f"""
Create an educational post explaining the philosophical school of {school}.

Format your response EXACTLY like this:

🎓 **Understanding {school}**

📚 **Core Principles:**
<Explain the 3-4 fundamental principles of {school} in clear, accessible language. Use bullet points with emojis.>

🌍 **Historical Context:**
<When did this school emerge? Who were the key thinkers? Why did it develop? 2-3 sentences.>

💡 **Key Insight:**
<Share one profound insight from {school} that challenges common thinking. Be specific and thought-provoking.>

🧘 **Practice:**
<How would a follower of {school} approach a modern dilemma or daily situation? Give a concrete example.>

#Philosophy #{school.replace(" ", "")} #PhilosophicalThinking

IMPORTANT:
- Be educational and accurate
- Make it accessible but not oversimplified
- Include real philosophical depth
- Avoid generic self-help language
"""


def get_philosopher_profile_prompt() -> str:
    """Generate a comprehensive profile of a philosopher."""
    seed = get_seed_from_timestamp()
    random.seed(seed)
    
    philosopher = random.choice(PHILOSOPHERS)
    
    return f"""
Create a compelling profile of the philosopher {philosopher}.

Format your response EXACTLY like this:

👤 **Philosopher Profile: {philosopher}**

⏳ **Era & Place:**
<When and where did they live? What was the historical context?>

🧠 **Central Ideas:**
<What were their 3-4 most important philosophical contributions? Be specific and clear.>

📖 **Famous Work:**
<Mention their most influential work or teaching and why it matters.>

💎 **Lasting Impact:**
<How did {philosopher} influence philosophy and human thought? What's their legacy?>

🎯 **One Powerful Question:**
<Pose one thought-provoking question that {philosopher} would ask us today.>

#Philosophy #{philosopher.replace(" ", "")} #Philosopher

IMPORTANT:
- Be factually accurate
- Highlight what makes this philosopher unique
- Make it engaging and educational
- Connect their ideas to timeless questions
"""


def get_philosophical_lesson_prompt() -> str:
    """Generate practical philosophical wisdom for modern life."""
    seed = get_seed_from_timestamp()
    random.seed(seed)
    
    philosopher = random.choice(PHILOSOPHERS)
    concept = random.choice(PHILOSOPHICAL_CONCEPTS)
    
    return f"""
Create a philosophical lesson that applies {philosopher}'s wisdom about {concept} to modern life.

Format your response EXACTLY like this:

🌟 **Philosophical Wisdom for Today**

🎭 **The Challenge:**
<Describe a common modern struggle or question related to {concept} that people face today. Make it relatable.>

🧙 **{philosopher}'s Perspective:**
<How would {philosopher} view this challenge? What would they say about {concept}? Include philosophical depth.>

💡 **The Insight:**
<Extract the key philosophical lesson. What does this teach us about thinking and living?>

🛤️ **Practical Application:**
<Give 2-3 concrete ways to apply this philosophical wisdom in daily life. Be specific and actionable.>

🤔 **Reflection Question:**
<End with a deep question for the reader to contemplate.>

#Philosophy #{concept.replace(" ", "")} #{philosopher.replace(" ", "")} #Wisdom

IMPORTANT:
- Bridge ancient wisdom with modern problems
- Be profound but practical
- Maintain philosophical rigor
- Avoid shallow self-help clichés
"""


def get_philosophical_debate_prompt() -> str:
    """Generate a post about philosophical debates and different perspectives."""
    seed = get_seed_from_timestamp()
    random.seed(seed)
    
    concept = random.choice(PHILOSOPHICAL_CONCEPTS)
    # Pick 2 different philosophers
    philosophers = random.sample(PHILOSOPHERS, 2)
    
    return f"""
Create a post exploring different philosophical perspectives on {concept}.

Format your response EXACTLY like this:

⚖️ **Philosophical Perspectives: {concept}**

🔍 **The Question:**
<Frame the central philosophical question about {concept}. Make it profound and universal.>

👨‍🏫 **{philosophers[0]}'s View:**
<How did {philosophers[0]} understand {concept}? What was their argument? Be specific.>

👨‍💼 **{philosophers[1]}'s View:**
<How did {philosophers[1]} approach {concept}? How does it differ from {philosophers[0]}?>

🎯 **The Tension:**
<What's at the heart of this philosophical disagreement? What fundamental assumptions differ?>

🌈 **Synthesis:**
<Is there wisdom in both views? How might we think about {concept} today, informed by both perspectives?>

#Philosophy #{concept.replace(" ", "")} #PhilosophicalDebate

IMPORTANT:
- Show real philosophical disagreement
- Be fair to both perspectives
- Demonstrate critical thinking
- Encourage readers to form their own views
"""


TEXT_TEMPLATES = {
    "quote": get_philosophical_quote_prompt,
    "thinking": get_philosophical_thinking_prompt,
    "profile": get_philosopher_profile_prompt,
    "lesson": get_philosophical_lesson_prompt,
    "debate": get_philosophical_debate_prompt
}
