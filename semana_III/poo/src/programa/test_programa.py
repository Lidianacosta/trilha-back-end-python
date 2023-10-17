from filme import Filme
from serie import Serie
from anime import Anime
from programa import Programa


Programa.adicionar_programa_a_lista(Anime('jujutsu kaisen', 2018, 2))
Programa.adicionar_programa_a_lista(Serie('Wandinha', 2022, 1))
Programa.adicionar_programa_a_lista(
    (Filme('A voz do silêncio', 2022, '2h 9m')))

Programa.listar_programas()
print()

anime = Programa.lista[0]
serie = Programa.lista[1]
filme = Programa.lista[2]

anime.dar_like()
anime.dar_like()
filme.dar_like()
filme.dar_like()
serie.dar_like()
serie.dar_like()

print(f'Anime: {anime.nome}, Ano: {anime.ano},'
      f'Temporadas: {anime.temporadas}, Likes: {anime.likes}')

print(f'Serie: {serie.nome}, Ano: {serie.ano}, '
      f'Temporadas: {serie.temporadas}, Likes: {serie.likes}')
print(
    f'Filme: {filme.nome}, Ano: {filme.ano}, '
    f'Duração {filme.duracao}, Likes: {filme.likes}')

print()

print(anime)
print(serie)
print(filme)
