import cv2

from detector import Detector
from loader.moviepy import MoviePy as Loader
from tracker import Tracker
from visualizer import Visualizer


def main():
    input_video_name = 'MVI_40855.mp4'
    input_video_folder = './unbox_test/input/'
    output_folder = './unbox_test/output/'

    loader = Loader(input_video_name, input_video_folder)
    tracker = Tracker(input_video_name, fps=loader.video.fps)
    loader_iter = loader.read_iter(batch_size=1)

    frames_count = int(loader.video.fps * loader.video.duration)

    detector = Detector(gpu_id=0)

    v1 = Visualizer()

    for i in range(frames_count):
        images, image_ids = next(loader_iter)
        frame = detector.detect(images, image_ids)[0]
        frame = tracker.track(frame)

        img_bgr = v1.draw_scene(frame)
        result_image_name = output_folder + str(i) + '.png'

        img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
        cv2.imwrite(result_image_name, img_rgb)

        print('[{0}/{1}] - {2}'.format(i, frames_count, result_image_name))
        pass
    print('done.')


if __name__ == "__main__":
    main()
