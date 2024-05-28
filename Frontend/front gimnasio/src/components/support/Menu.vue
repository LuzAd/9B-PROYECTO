    <template>

    ...
    <li>
        <a
        href="#"
        @click.prevent="updateMenu('products')"
        :class="highlightSection('products')"
        >
          <i class="fa fa-tag menu__icon" aria-hidden="true"></i>
          Products
          <i class="fa fa-chevron-right menu__arrow-icon" aria-hidden="true"></i>
        </a>
    </li>
    ...

    </template>