#!/usr/bin/env python

import fcis


def main():
    fcis.models.FCISResNet101.download('coco')


if __name__ == '__main__':
    main()
