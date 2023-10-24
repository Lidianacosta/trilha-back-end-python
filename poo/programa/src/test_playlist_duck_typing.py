from filme import Filme
from serie import Serie
from anime import Anime
from playlist import Playlist


playlist_ferias = Playlist(
    'Férias', [
        Anime('jujutsu kaisen', 2018, 2),
        Serie('Wandinha', 2022, 1),
        Filme('A voz do silêncio', 2022, '2h 9m')
    ]
)

playlist_ferias[0].dar_like()
playlist_ferias[0].dar_like()
playlist_ferias[1].dar_like()
playlist_ferias[1].dar_like()
playlist_ferias[2].dar_like()
playlist_ferias[2].dar_like()


print(
    f'Nome da playlist: {playlist_ferias.nome}, '
    f'programas: {len(playlist_ferias)}')
print('programas: ')
for programa in playlist_ferias:
    print(programa)
