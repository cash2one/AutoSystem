# encoding: utf-8
"""Convert caption files to different formats

One or more caption files will be converted to the specified output format,
saved next to the input file

Requires the pycaption library from PBS: https://pypi.python.org/pypi/pycaption/
"""

from __future__ import absolute_import, print_function, unicode_literals

import logging
import os
import sys
from argparse import ArgumentParser, FileType

try:
    import pycaption
except ImportError:
    print('Unable to import pycaption: have you installed it?', file=sys.stderr)
    raise

SUPPORTED_WRITERS = {
    'dfxp': pycaption.DFXPWriter,
    'sami': pycaption.SAMIWriter,
    'srt': pycaption.SRTWriter,
    'scc': pycaption.SCCWriter,
    'webvtt': pycaption.WebVTTWriter,
}

FILE_EXTENSIONS = {
    'dfxp': 'dfxp.xml',
    'sami': 'sami',
    'srt': 'srt',
    'scc': 'scc',
    'webvtt': 'vtt',
}


def convert_file(input_captions, output_writer):
    reader = pycaption.detect_format(input_captions)

    if not reader:
        raise RuntimeError('Unrecognized format')

    converter = pycaption.CaptionConverter()
    converter.read(input_captions, reader())
    return converter.write(output_writer)

# todo,未完成，现在使用ffmpeg的转化字幕功能subtitle.py convert_subtilte_format
def convert_subtilte_format(input_file, output_format):
    # 根据需要转换的字幕格式，选择pycaption库对应的类
    output_writer_class = SUPPORTED_WRITERS[output_format]

    output_file = '%s.%s' % (os.path.splitext(input_file)[0],
                             FILE_EXTENSIONS[output_format])

    with open(output_file, 'wb') as output_f:
        funicode = input_file.read()
        output_f.write(
            convert_file(funicode.decode('utf-8'), output_writer_class()))


if __name__ == "__main__":
    parser = ArgumentParser(description=__doc__.strip())
    parser.add_argument('--output-format', type=lambda i: i.lower(),
                        metavar='FORMAT', default='WebVTT',
                        choices=SUPPORTED_WRITERS.keys(),
                        help='Output format: %(choices)s (default: %('
                             'default)s)')
    parser.add_argument('caption_file', type=FileType('r'), nargs='+',
                        help='Caption files to convert')
    args = parser.parse_args()

    if args.output_format not in SUPPORTED_WRITERS:
        parser.error('Output format must be one of %s' % ' '.join(
            SUPPORTED_WRITERS.keys()))
    else:
        output_writer_class = SUPPORTED_WRITERS[args.output_format]

    logging.basicConfig()

    for f in args.caption_file:
        output_file = '%s.%s' % (os.path.splitext(f.name)[0],
                                 FILE_EXTENSIONS[args.output_format])

        print(output_file)

        try:
            with open(output_file, 'wb') as output_f:
                funicode = f.read()
                output_f.write(convert_file(funicode.decode('utf-8'),
                                            output_writer_class()))
        except Exception as exc:
            import pdb;

            pdb.post_mortem(sys.exc_info()[2])
            logging.error('Unable to convert %s: %s', f.name, exc)
            f.close()
            continue
