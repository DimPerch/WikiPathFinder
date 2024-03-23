from wiki_path_finder import WikiPathFinder


if __name__ == "__main__":
    finder = WikiPathFinder("https://ru.wikipedia.org/wiki/Санкт-Петербургский_государственный_электротехнический_университет",
                            "https://ru.wikipedia.org/wiki/Философия")
    finder.find()
