from unittest import TestCase, main

from project.social_media import SocialMedia


class TestSocialMedia(TestCase):

    def setUp(self):
        self.social_media = SocialMedia("user_oleg", "Instagram", 1000, "picture")

    def test_correct_init(self):
        self.assertEqual("user_oleg", self.social_media._username)
        self.assertEqual("Instagram", self.social_media._platform)
        self.assertEqual(1000, self.social_media._followers)
        self.assertEqual("picture", self.social_media._content_type)
        self.assertEqual([], self.social_media._posts)

    def test_set_followers_positive(self):
        self.social_media.followers = 2000
        self.assertEqual(self.social_media.followers, 2000)

    def test_set_followers_zero(self):
        self.social_media.followers = 0
        self.assertEqual(self.social_media.followers, 0)

    def test_set_followers_negative_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.social_media.followers = -1
        self.assertEqual("Followers cannot be negative.", str(ex.exception))

    def test_set_followers_invalid_type(self):
        with self.assertRaises(TypeError):
            self.social_media.followers = "1000"

    def test_valid_platform(self):
        valid_platforms = ['Instagram', 'YouTube', 'Twitter']
        for platform in valid_platforms:
            self.social_media._validate_and_set_platform(platform)
            self.assertEqual(self.social_media._platform, platform)

    def test_invalid_platform_raises(self):
        invalid_platform = 'Facebook'
        with self.assertRaises(ValueError):
            self.social_media._validate_and_set_platform(invalid_platform)

    def test_create_post_new_return(self):
        self.assertEqual(self.social_media.create_post("Test post"),
                         "New picture post created by user_oleg on Instagram.")
        self.assertEqual(len(self.social_media._posts), 1)

    def test_like_post_return(self):
        self.social_media.create_post("Test post")
        self.assertEqual(self.social_media.like_post(0), "Post liked by user_oleg.")
        self.assertEqual(self.social_media.like_post(0), "Post liked by user_oleg.")

    #def test_like_post_more_than_max_likes(self):
        # # Test maximum likes
        # for i in range(10):
        #     self.assertEqual(self.social_media.like_post(0), "Post has reached the maximum number of likes.")
        # self.assertEqual(self.social_media.like_post(0), "Invalid post index.")

    def test_comment_on_post_return(self):
        self.social_media.create_post("Test post")
        self.assertEqual(self.social_media.comment_on_post(0, "Nice post!"),
                         "Comment should be more than 10 characters.")
        self.assertEqual(self.social_media.comment_on_post(0, "This is a nice post!"),
                         "Comment added by user_oleg on the post.")
        self.assertEqual(len(self.social_media._posts[0]['comments']), 1)


if __name__ == '__main__':
    main()
