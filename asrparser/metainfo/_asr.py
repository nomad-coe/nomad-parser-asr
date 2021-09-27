#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD.
# See https://nomad-lab.eu for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import numpy as np            # pylint: disable=unused-import
import typing                 # pylint: disable=unused-import
from nomad.metainfo import (  # pylint: disable=unused-import
    MSection, MCategory, Category, Package, Quantity, Section, SubSection, SectionProxy,
    Reference
)

from nomad.datamodel.metainfo import simulation


m_package = Package()


class Parameters(MSection):

    m_def = Section(validate=False)

    x_asr_tmp_atoms_file = Quantity(
        type=str,
        shape=[],
        description='''
        ''')

    x_asr_d3 = Quantity(
        type=bool,
        shape=[],
        description='''
        ''')

    x_asr_fixcell = Quantity(
        type=bool,
        shape=[],
        description='''
        ''')

    x_asr_allow_symmetry_breaking = Quantity(
        type=bool,
        shape=[],
        description='''
        ''')

    x_asr_fmax = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ''')

    x_asr_enforce_symmetry = Quantity(
        type=bool,
        shape=[],
        description='''
        ''')


class Code(MSection):

    m_def = Section(validate=False)

    x_asr_package = Quantity(
        type=str,
        shape=[],
        description='''
        ''')

    x_asr_version = Quantity(
        type=str,
        shape=[],
        description='''
        ''')

    x_asr_git_hash = Quantity(
        type=str,
        shape=[],
        description='''
        ''')


class RunSpecification(MSection):

    m_def = Section(validate=False)

    x_asr_name = Quantity(
        type=str,
        shape=[],
        description='''
        ''')

    x_asr_uid = Quantity(
        type=str,
        shape=[],
        description='''
        ''')

    x_asr_version = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ''')

    x_asr_codes = SubSection(sub_section=Code.m_def, repeats=True)

    x_asr_parameters = SubSection(sub_section=Parameters.m_def, repeats=True)


class Resources(MSection):

    m_def = Section(validate=False)

    x_asr_execution_duration = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ''')




class Run(simulation.run.Run):

    m_def = Section(validate=False, extends_base_section=True)

    x_asr_emmet_version = Quantity(
        type=str,
        shape=[],
        description='''
        ''')



    x_asr_run_specification = SubSection(sub_section=RunSpecification.m_def)


