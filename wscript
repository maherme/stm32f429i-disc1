#! /usr/bin/env python
# encoding: utf-8

top = '.'
out = 'build'

app_name = 'stm32f429i-disc1'
source_files = [
    'src/startup_stm32f429zitx.s',
    'src/systeminit.c',
    'src/main.c',
    'src/hlp/logger.c',
    'src/drv/usb/usb_driver.c',
    'src/drv/gpio/gpio_driver.c',
    'src/mid/usb/usb_middleware.c'
]
include_path = [
    'inc/CMSIS/Device/ST/STM32F4xx/Include',
    'inc/CMSIS/Include',
    'src',
    'src/hlp',
    'src/drv/usb',
    'src/drv/gpio',
    'src/mid/usb'
]

def configure(cnf):
    cnf.load('gcc_flags armgcc c', tooldir='wafconf')

    target_flags = [
        "-mcpu=cortex-m4",
        "-mthumb",
        "-mfpu=fpv4-sp-d16",
        "-mfloat-abi=hard"
    ]

    cnf.env.LINKFLAGS.extend(target_flags)
    cnf.env.CPPFLAGS.extend(target_flags)

def build(bld):
    bld.program(
        source   = source_files,
        includes = include_path,
        target   = app_name + '.elf'
    )
    bld(
        source = app_name + '.elf', 
        target = app_name + '.hex'
    )