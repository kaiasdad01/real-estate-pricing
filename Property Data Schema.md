Property Data Schema

This page contains a data dictionary and a description of all response fields for our property data endpoints (`/properties`).

<HTMLBlock>{`
&nbsp;
`}</HTMLBlock>

## Property Records Response Fields

The following response fields will be returned as part of property records:

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Response Field
      </th>

      <th>
        Description
      </th>

      <th>
        Example Value
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `id`
      </td>

      <td>
        Property Id
        *Data type: String*

        A unique RentCast property identifier
      </td>

      <td>
        `"5500-Grand-Lake-Dr,-San-Antonio,-TX-78244"`
      </td>
    </tr>

    <tr>
      <td>
        `formattedAddress`
      </td>

      <td>
        Formatted Address\
        *Data type: String*

        The full property address, in the format `Street, Unit, City, State Zip`
      </td>

      <td>
        `"5500 Grand Lake Dr, San Antonio, TX 78244"`
      </td>
    </tr>

    <tr>
      <td>
        `addressLine1`
      </td>

      <td>
        Address Line 1\
        *Data type: String*

        The first line of the property street address
      </td>

      <td>
        `"5500 Grand Lake Dr"`
      </td>
    </tr>

    <tr>
      <td>
        `addressLine2`
      </td>

      <td>
        Address Line 2\
        *Data type: String*

        The second line of the property street address, typically containing the unit or apartment identifier
      </td>

      <td>
        `"Apt 12"`
      </td>
    </tr>

    <tr>
      <td>
        `city`
      </td>

      <td>
        Address City\
        *Data type: String*

        The city of the property address
      </td>

      <td>
        `"San Antonio"`
      </td>
    </tr>

    <tr>
      <td>
        `state`
      </td>

      <td>
        Address State\
        *Data type: String*

        The state of the property address, as a 2-character abbreviation
      </td>

      <td>
        `"TX"`
      </td>
    </tr>

    <tr>
      <td>
        `zipCode`
      </td>

      <td>
        Address Zip Code\
        *Data type: String*

        The 5-digit zip code of the property address
      </td>

      <td>
        `"78244"`
      </td>
    </tr>

    <tr>
      <td>
        `county`
      </td>

      <td>
        County\
        *Data type: String*

        The county in which the property is located
      </td>

      <td>
        `"Bexar"`
      </td>
    </tr>

    <tr>
      <td>
        `latitude`
      </td>

      <td>
        Latitude\
        *Data type: Number*

        The latitude of the property's geographical location
      </td>

      <td>
        `29.476011`
      </td>
    </tr>

    <tr>
      <td>
        `longitude`
      </td>

      <td>
        Longitude\
        *Data type: Number*

        The longitude of the property's geographical location
      </td>

      <td>
        `-98.351454`
      </td>
    </tr>

    <tr>
      <td>
        `propertyType`
      </td>

      <td>
        Property Type\
        *Data type: String (Enum)*

        The type of the property. See [explanation of property types](https://developers.rentcast.io/reference/property-types) for possible values
      </td>

      <td>
        `"Single Family"`
      </td>
    </tr>

    <tr>
      <td>
        `bedrooms`
      </td>

      <td>
        Number of Bedrooms\
        *Data type: Number*

        The number of bedrooms in the property, with a value of "0" indicating a studio layout
      </td>

      <td>
        `3`
      </td>
    </tr>

    <tr>
      <td>
        `bathrooms`
      </td>

      <td>
        Number of Bathrooms\
        *Data type: Number*

        The number of bathrooms in the property
      </td>

      <td>
        `2`
      </td>
    </tr>

    <tr>
      <td>
        `squareFootage`
      </td>

      <td>
        Living Area (Sq.Ft.)\
        *Data type: Number*

        The total indoor living area of the property, in square feet
      </td>

      <td>
        `1878`
      </td>
    </tr>

    <tr>
      <td>
        `lotSize`
      </td>

      <td>
        Lot Area (Sq.Ft.)\
        *Data type: Number*

        The total lot size of the property parcel, in square feet
      </td>

      <td>
        `8843`
      </td>
    </tr>

    <tr>
      <td>
        `yearBuilt`
      </td>

      <td>
        Year Built\
        *Data type: Number*

        The year in which the property was constructed
      </td>

      <td>
        `1973`
      </td>
    </tr>

    <tr>
      <td>
        `assessorID`
      </td>

      <td>
        Assessor Id\
        *Data type: String*

        The county assessor identifier or assessor parcel number (APN) of the property
      </td>

      <td>
        `"05076-103-0500"`
      </td>
    </tr>

    <tr>
      <td>
        `legalDescription`
      </td>

      <td>
        Legal Description\
        *Data type: String*

        The legal description of the property, as provided by county records
      </td>

      <td>
        `"CB 5076A BLK 3 LOT 50"`
      </td>
    </tr>

    <tr>
      <td>
        `subdivision`
      </td>

      <td>
        Subdivision\
        *Data type: String*

        The subdivision identifier of the property, as provided by county records
      </td>

      <td>
        `"CONV A/S CODE"`
      </td>
    </tr>

    <tr>
      <td>
        `zoning`
      </td>

      <td>
        Zoning Code\
        *Data type: String*

        The zoning code or description of the property, as provided by county records
      </td>

      <td>
        `"RH"`
      </td>
    </tr>

    <tr>
      <td>
        `lastSaleDate`
      </td>

      <td>
        Last Sale Date\
        *Data type: Date*

        The date the property was last sold, in ISO 8601 format
      </td>

      <td>
        `"2017-10-19T00:00:00.000Z"`
      </td>
    </tr>

    <tr>
      <td>
        `lastSalePrice`
      </td>

      <td>
        Last Sale Price\
        *Data type: Number*

        The last known sale price of the property
      </td>

      <td>
        `185000`
      </td>
    </tr>

    <tr>
      <td>
        `hoa`
      </td>

      <td>
        HOA Details\
        *Data type: Object*

        Information about the property's homeowner's association (HOA)
      </td>

      <td>
        `{ ... }`
      </td>
    </tr>

    <tr>
      <td>
        `hoa.fee`
      </td>

      <td>
        HOA Fee Amount (Monthly)\
        *Data type: Number*

        The total monthly HOA fee or assessment amount
      </td>

      <td>
        `175`
      </td>
    </tr>

    <tr>
      <td>
        `features`
      </td>

      <td>
        Property Features\
        *Data type: Object*

        A list of property features and characteristics
      </td>

      <td>
        `{ ... }`
      </td>
    </tr>

    <tr>
      <td>
        ```
        features
        .architectureType
        ```
      </td>

      <td>
        Feature - Architecture Type\
        *Data type: String*

        The architecture type of the property, as provided by county records. See [list of architecture types](#architecture-types-featuresarchitecturetype) for possible values
      </td>

      <td>
        `"Contemporary"`
      </td>
    </tr>

    <tr>
      <td>
        `features.cooling`
      </td>

      <td>
        Feature - Cooling\
        *Data type: Boolean*

        A field indicating whether or not the property has a cooling system
      </td>

      <td>
        `true`
      </td>
    </tr>

    <tr>
      <td>
        ```
        features
        .coolingType
        ```
      </td>

      <td>
        Feature - Cooling Type\
        *Data type: String*

        The type of the cooling system installed at the property, as provided by county records. See [list of cooling types](#cooling-types-featurescoolingtype) for possible values
      </td>

      <td>
        `"Central"`
      </td>
    </tr>

    <tr>
      <td>
        ```
        features
        .exteriorType
        ```
      </td>

      <td>
        Feature - Exterior Type\
        *Data type: String*

        The exterior type of the property, as provided by county records. See [list of exterior types](#exterior-types-featuresexteriortype) for possible values
      </td>

      <td>
        `"Wood"`
      </td>
    </tr>

    <tr>
      <td>
        `features.fireplace`
      </td>

      <td>
        Feature - Fireplace\
        *Data type: Boolean*

        A field indicating whether or not the property has a fireplace
      </td>

      <td>
        `true`
      </td>
    </tr>

    <tr>
      <td>
        ```
        features
        .fireplaceType
        ```
      </td>

      <td>
        Feature - Fireplace Type\
        *Data type: String*

        The type of fireplace installed at the property, as provided by county records. See list of [fireplace types](#fireplace-types-featuresfireplacetype) for possible values
      </td>

      <td>
        `"Masonry"`
      </td>
    </tr>

    <tr>
      <td>
        `features.floorCount`
      </td>

      <td>
        Feature - Floor Count\
        *Data type: Number*

        The number of above-ground floors or stories in the property
      </td>

      <td>
        `1`
      </td>
    </tr>

    <tr>
      <td>
        ```
        features
        .foundationType
        ```
      </td>

      <td>
        Feature - Foundation Type\
        *Data type: String*

        The foundation type of the property, as provided by county records. See [list of foundation types](#foundation-types-featuresfoundationtype) for possible values
      </td>

      <td>
        `"Slab / Mat / Raft"`
      </td>
    </tr>

    <tr>
      <td>
        `features.garage`
      </td>

      <td>
        Feature - Garage\
        *Data type: Boolean*

        A field indicating whether or not the property has a garage
      </td>

      <td>
        `true`
      </td>
    </tr>

    <tr>
      <td>
        ```
        features
        .garageSpaces
        ```
      </td>

      <td>
        Feature - Garage Spaces\
        *Data type: Number*

        The number of garage spaces in the property
      </td>

      <td>
        `2`
      </td>
    </tr>

    <tr>
      <td>
        `features.garageType`
      </td>

      <td>
        Feature - Garage Type\
        *Data type: String*

        The garage type of the property, as provided by county records. See [list of garage types](#garage-types-featuresgaragetype) for possible values
      </td>

      <td>
        `"Garage"`
      </td>
    </tr>

    <tr>
      <td>
        `features.heating`
      </td>

      <td>
        Feature - Heating\
        *Data type: Boolean*

        A field indicating whether or not the property has a heating system
      </td>

      <td>
        `true`
      </td>
    </tr>

    <tr>
      <td>
        ```
        features
        .heatingType
        ```
      </td>

      <td>
        Feature - Heating Type\
        *Data type: String*

        The type of the heating system installed at the property, as provided by county records. See [list of heating types](#heating-types-featuresheatingtype) for possible values
      </td>

      <td>
        `"Forced Air"`
      </td>
    </tr>

    <tr>
      <td>
        `features.pool`
      </td>

      <td>
        Feature - Pool\
        *Data type: Boolean*

        A field indicating whether or not the property has a pool
      </td>

      <td>
        `true`
      </td>
    </tr>

    <tr>
      <td>
        `features.poolType`
      </td>

      <td>
        Feature - Pool Type\
        *Data type: String*

        The pool type of the property, as provided by county records. See [list of pool types](#pool-types-featurespooltype) for possible values
      </td>

      <td>
        `"Concrete"`
      </td>
    </tr>

    <tr>
      <td>
        `features.roofType`
      </td>

      <td>
        Feature - Roof Type\
        *Data type: String*

        The roof type of the property, as provided by county records. See [list of roof types](#roof-types-featuresrooftype) for possible values
      </td>

      <td>
        `"Asphalt"`
      </td>
    </tr>

    <tr>
      <td>
        `features.roomCount`
      </td>

      <td>
        Feature - Room Count\
        *Data type: Number*

        The number of interior rooms in the property, including bedrooms, living rooms, dens, kitchens and dining rooms
      </td>

      <td>
        `5`
      </td>
    </tr>

    <tr>
      <td>
        `features.unitCount`
      </td>

      <td>
        Feature - Unit Count\
        *Data type: Number*

        The number of individual units in the property, if it is a multi-dwelling building
      </td>

      <td>
        `1`
      </td>
    </tr>

    <tr>
      <td>
        `features.viewType`
      </td>

      <td>
        Feature - View Type\
        *Data type: String*

        The type of view of the property, as provided by county records. See [list of view types](#view-types-featuresviewtype) for possible values
      </td>

      <td>
        `"City"`
      </td>
    </tr>

    <tr>
      <td>
        `taxAssessments`
      </td>

      <td>
        Tax Assessments\
        *Data type: Object*

        A list of tax assessments for this property, with JSON keys indicating the tax year, in the format `YYYY`
      </td>

      <td>
        `{ "2023": { ... } }`
      </td>
    </tr>

    <tr>
      <td>
        `taxAssessments[YYYY]`
      </td>

      <td>
        Tax Assessment Entry\
        *Data type: Object*

        A single tax assessment entry, with data for a specific tax year
      </td>

      <td>
        `{ ... }`
      </td>
    </tr>

    <tr>
      <td>
        ```
        taxAssessments[YYYY]
        .year
        ```
      </td>

      <td>
        Tax Assessment Entry - Year\
        *Data type: Number*

        The tax assessment year
      </td>

      <td>
        `2023`
      </td>
    </tr>

    <tr>
      <td>
        ```
        taxAssessments[YYYY]
        .value
        ```
      </td>

      <td>
        Tax Assessment Entry - Total Assessment\
        *Data type: Number*

        The total assessed value of the property, including land and improvements
      </td>

      <td>
        `225790`
      </td>
    </tr>

    <tr>
      <td>
        ```
        taxAssessments[YYYY]
        .land
        ```
      </td>

      <td>
        Tax Assessment Entry - Land Assessment\
        *Data type: Number*

        The assessed value of the land
      </td>

      <td>
        `59380`
      </td>
    </tr>

    <tr>
      <td>
        ```
        taxAssessments[YYYY]
        .improvements
        ```
      </td>

      <td>
        Tax Assessment Entry - Improvements Assessment\
        *Data type: Number*

        The assessed value of the building and improvements
      </td>

      <td>
        `166410`
      </td>
    </tr>

    <tr>
      <td>
        `propertyTaxes`
      </td>

      <td>
        Property Taxes\
        *Data type: Object*

        A list of property taxes for this property, with JSON keys indicating the tax year, in the format `YYYY`
      </td>

      <td>
        `{ "2023": { ... } }`
      </td>
    </tr>

    <tr>
      <td>
        `propertyTaxes[YYYY]`
      </td>

      <td>
        Property Tax Entry\
        *Data type: Object*

        A single property tax entry, with data for a specific tax year
      </td>

      <td>
        `{ ... }`
      </td>
    </tr>

    <tr>
      <td>
        ```
        propertyTaxes[YYYY]
        .year
        ```
      </td>

      <td>
        Property Tax Entry - Year\
        *Data type: Number*

        The property tax year
      </td>

      <td>
        `2023`
      </td>
    </tr>

    <tr>
      <td>
        ```
        propertyTaxes[YYYY]
        .total
        ```
      </td>

      <td>
        Property Tax Entry - Total Tax\
        *Data type: Number*

        The total annual property tax amount
      </td>

      <td>
        `4201`
      </td>
    </tr>

    <tr>
      <td>
        `history`
      </td>

      <td>
        Property History\
        *Data type: Object*

        A list of sale transactions for this property, with JSON keys indicating the sale date, in the format `YYYY-MM-DD`
      </td>

      <td>
        `{ "2017-10-19": { ... } }`
      </td>
    </tr>

    <tr>
      <td>
        `history[YYYY-MM-DD]`
      </td>

      <td>
        Property History Entry\
        *Data type: Object*

        A single sale transaction entry, with historical property sale information
      </td>

      <td>
        `{ ... }`
      </td>
    </tr>

    <tr>
      <td>
        ```
        history[YYYY-MM-DD]
        .event
        ```
      </td>

      <td>
        Property History Entry - Event Type\
        *Data type: String (Enum)*

        The type of the transaction, with the only possible value of "Sale"
      </td>

      <td>
        `"Sale"`
      </td>
    </tr>

    <tr>
      <td>
        ```
        history[YYYY-MM-DD]
        .date
        ```
      </td>

      <td>
        Property History Entry - Sale Date\
        *Data type: Number*

        The date the property was sold, in ISO 8601 format
      </td>

      <td>
        `"2017-10-19T00:00:00.000Z"`
      </td>
    </tr>

    <tr>
      <td>
        ```
        history[YYYY-MM-DD]
        .price
        ```
      </td>

      <td>
        Property History Entry - Sale Price\
        *Data type: Number*

        The sale price of the property
      </td>

      <td>
        `185000`
      </td>
    </tr>

    <tr>
      <td>
        `owner`
      </td>

      <td>
        Property Owner Details\
        *Data type: Object*

        Information about the current owner(s) of this property
      </td>

      <td>
        `{ ... }`
      </td>
    </tr>

    <tr>
      <td>
        `owner.names`
      </td>

      <td>
        Property Owner - Names\
        *Data type: Array*

        A list of names of the individuals or organizations listed as the current property owner(s). Individual owner names will typically be in the format `First Middle Last`
      </td>

      <td>
        `[ "Michael Smith" ]`
      </td>
    </tr>

    <tr>
      <td>
        `owner.type`
      </td>

      <td>
        Property Owner - Entity Type\
        *Data type: String (Enum)*

        The type of the current property owner(s), with possible values of "Individual" for individuals or persons, or "Organization" for other types of entities
      </td>

      <td>
        `"Individual"`
      </td>
    </tr>

    <tr>
      <td>
        `owner.mailingAddress`
      </td>

      <td>
        Property Owner - Mailing Address\
        *Data type: Object*

        The mailing address of the current property owner(s)
      </td>

      <td>
        `{ ... }`
      </td>
    </tr>

    <tr>
      <td>
        ```
        owner.mailingAddress
        .id
        ```
      </td>

      <td>
        Property Owner - Mailing Address Id\
        *Data type: String*

        A unique RentCast property identifier
      </td>

      <td>
        `"149-Weaver-Blvd,---264,-Weaverville,-NC-28787"`
      </td>
    </tr>

    <tr>
      <td>
        ```
        owner.mailingAddress
        .formattedAddress
        ```
      </td>

      <td>
        Property Owner - Mailing Address Formatted\
        *Data type: String*

        The full property address, in the format `Street, Unit, City, State Zip`
      </td>

      <td>
        `"149 Weaver Blvd, # 264, Weaverville, NC 28787"`
      </td>
    </tr>

    <tr>
      <td>
        ```
        owner.mailingAddress
        .addressLine1
        ```
      </td>

      <td>
        Property Owner - Mailing Address Line 1\
        *Data type: String*

        The first line of the property street address
      </td>

      <td>
        `"149 Weaver Blvd"`
      </td>
    </tr>

    <tr>
      <td>
        ```
        owner.mailingAddress
        .addressLine2
        ```
      </td>

      <td>
        Property Owner - Mailing Address Line 2\
        *Data type: String*

        The second line of the property street address, typically containing the unit or apartment identifier
      </td>

      <td>
        `"# 264"`
      </td>
    </tr>

    <tr>
      <td>
        ```
        owner.mailingAddress
        .city
        ```
      </td>

      <td>
        Property Owner - Mailing Address City\
        *Data type: String*

        The city of the property address
      </td>

      <td>
        `"Weaverville"`
      </td>
    </tr>

    <tr>
      <td>
        ```
        owner.mailingAddress
        .state
        ```
      </td>

      <td>
        Property Owner - Mailing Address State\
        *Data type: String*

        The state of the property address, as a 2-character abbreviation
      </td>

      <td>
        `"NC"`
      </td>
    </tr>

    <tr>
      <td>
        ```
        owner.mailingAddress
        .zipCode
        ```
      </td>

      <td>
        Property Owner - Mailing Address Zip Code\
        *Data type: String*

        The 5-digit zip code of the property address
      </td>

      <td>
        `"28787"`
      </td>
    </tr>

    <tr>
      <td>
        `ownerOccupied`
      </td>

      <td>
        Owner Occupied Status\
        *Data type: Boolean*

        A field indicating whether the property is currently occupied by its property owner(s)
      </td>

      <td>
        `false`
      </td>
    </tr>
  </tbody>
</Table>

> 📘
>
> Data availability of specific property record fields may vary by county and state. Our API will always return all available fields and data for each property.

<HTMLBlock>{`
&nbsp;
`}</HTMLBlock>

## Property Feature Field Values

Our property data endpoints return several descriptive property features and characteristics in the `features` response field, when available.

We obtain this data directly from public county records, and apply light standardization and formatting to the values of these fields to improve their consistency across various counties.

While the following lists provide the majority of possible field values with the `String` data type, you may encounter other values if they have been recently added by the upstream county record databases. In such cases, we encourage you to [contact us](mailto:support@rentcast.io) so we can update our documentation.

> 📘
>
> The response fields listed below may contain multiple values in the same JSON string, separated by the forward slash character (`/`).

<br />

### Architecture Types (`features.architectureType`)

| Possible Values       |
| :-------------------- |
| `Apartment`           |
| `Bi-Level`            |
| `Bungalow`            |
| `Cape Cod`            |
| `Colonial`            |
| `Condo`               |
| `Contemporary`        |
| `Conventional`        |
| `Cottage`             |
| `Custom`              |
| `Duplex`              |
| `European`            |
| `High Rise`           |
| `Historical`          |
| `High Rise`           |
| `Mobile Home`         |
| `Modern`              |
| `Multi-Unit Building` |
| `Other`               |
| `Raised Ranch`        |
| `Rambler`             |
| `Ranch`               |
| `Spanish`             |
| `Split Level`         |
| `Townhouse`           |
| `Traditional`         |
| `Triplex`             |

<br />

### Cooling Types (`features.coolingType`)

| Possible Values |
| :-------------- |
| `Central`       |
| `Commercial`    |
| `Evaporative`   |
| `Other`         |
| `Package`       |
| `Refrigeration` |
| `Wall`          |
| `Window`        |

<br />

### Exterior Types (`features.exteriorType`)

| Possible Values    |
| :----------------- |
| `Aluminum`         |
| `Aluminum Siding`  |
| `Asbestos Shingle` |
| `Block`            |
| `Brick`            |
| `Brick Veneer`     |
| `Combination`      |
| `Composition`      |
| `Concrete`         |
| `Concrete Block`   |
| `Frame`            |
| `Frame Siding`     |
| `Marble`           |
| `Marblecrete`      |
| `Masonry`          |
| `Metal`            |
| `Other`            |
| `Shingle`          |
| `Siding`           |
| `Stone`            |
| `Stucco`           |
| `Vinyl`            |
| `Vinyl Siding`     |
| `Wood`             |
| `Wood Frame`       |
| `Wood Shingle`     |

<br />

### Fireplace Types (`features.fireplaceType`)

| Possible Values         |
| :---------------------- |
| `1 Story`               |
| `1 Story Brick Chimney` |
| `2 Story`               |
| `2 Story Brick Chimney` |
| `Backed`                |
| `Gas Log`               |
| `Masonry`               |
| `Other`                 |
| `Prefab`                |
| `Single`                |

<br />

### Foundation Types (`features.foundationType`)

| Possible Values  |
| :--------------- |
| `Block`          |
| `Concrete`       |
| `Concrete Block` |
| `Crawl`          |
| `Footing`        |
| `Masonry`        |
| `Mat`            |
| `Other`          |
| `Pier`           |
| `Pile`           |
| `Post & Beam`    |
| `Raft`           |
| `Raised`         |
| `Slab`           |
| `Stone`          |
| `Wood`           |

<br />

### Garage Types (`features.garageType`)

| Possible Values |
| :-------------- |
| `Attached`      |
| `Basement`      |
| `Built-in`      |
| `Carport`       |
| `Detached`      |
| `Garage`        |
| `Mixed`         |
| `Other`         |
| `Underground`   |

<br />

### Heating Types (`features.heatingType`)

| Possible Values |
| :-------------- |
| `Baseboard`     |
| `Central`       |
| `Electric`      |
| `Floor`         |
| `Forced Air`    |
| `Furnace`       |
| `Gas`           |
| `Heat Pump`     |
| `Hot Water`     |
| `Oil`           |
| `Other`         |
| `Package`       |
| `Radiant`       |
| `Steam`         |
| `Wall`          |

<br />

### Pool Types (`features.poolType`)

| Possible Values        |
| :--------------------- |
| `Above-Ground Pool`    |
| `Community Pool`       |
| `Concrete`             |
| `Fiberglass`           |
| `Gunite`               |
| `Heated Pool`          |
| `In-Ground Pool`       |
| `In-Ground Vinyl Pool` |
| `Indoor Pool`          |
| `Municipal`            |
| `Other`                |
| `Plastic`              |
| `Pool and Hot Tub`     |
| `Public`               |
| `Reinforced Concrete`  |
| `Spa`                  |

<br />

### Roof Types (`features.roofType`)

| Possible Values       |
| :-------------------- |
| `Aluminum`            |
| `Asbestos`            |
| `Asphalt`             |
| `Built-up`            |
| `Composition Shingle` |
| `Concrete`            |
| `Concrete Tile`       |
| `Fiberglass`          |
| `Gravel`              |
| `Metal`               |
| `Other`               |
| `Roll Composition`    |
| `Shake`               |
| `Shingle`             |
| `Slate`               |
| `Tile`                |
| `Wood`                |
| `Wood Shake`          |
| `Wood Shingle`        |

<br />

### View Types (`features.viewType`)

| Possible Values |
| :-------------- |
| `Average`       |
| `Beach`         |
| `Canal`         |
| `City`          |
| `Corner`        |
| `Cul-de-sac`    |
| `Excellent`     |
| `Fair`          |
| `Golf Course`   |
| `Good`          |
| `Lake`          |
| `Mountain`      |
| `Other`         |
| `Park`          |
| `River`         |
| `Water`         |
| `Waterfront`    |

<HTMLBlock>{`
&nbsp;
`}</HTMLBlock>