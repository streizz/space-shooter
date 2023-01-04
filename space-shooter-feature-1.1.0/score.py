import pygame.font


class Score:
    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.font = pygame.font.SysFont(None, 42)
        self.stats = stats

    def image_score(self):
        self.score_image = self.font.render(str(self.stats.score), True, (201, 99, 198), (0, 0, 0))
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 30
        self.score_rect.top = 20

    def image_high_score(self):
        self.score_high_image = self.font.render(str(self.stats.high_score), True, (255, 50, 198), (0, 0, 0))
        self.score_high_rect = self.score_high_image.get_rect()
        self.score_high_rect.centerx = self.screen_rect.centerx
        self.score_high_rect.top = 20


    def render(self):
        self.image_score()
        self.image_high_score()
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.score_high_image, self.score_high_rect)
